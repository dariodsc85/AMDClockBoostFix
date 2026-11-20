# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMD Clock Boost Fix contributors
from __future__ import annotations

import argparse
import ctypes
import gc
import json
import os
import re
import subprocess
import sys
import threading
import time
import tkinter as tk
import winreg
from pathlib import Path
from tkinter import messagebox, ttk
from typing import Any

APP = "AMDClockBoostFix"
APP_VERSION = "2.4"  # Controle interno de versão (não exposto na interface gráfica)
LEGACY_APP = "RX7600ClockHelper"
BASE = Path(__file__).resolve().parent
BUNDLE_ROOT = Path(getattr(sys, "_MEIPASS", BASE))
ICON_RELATIVE_PATH = Path("assets") / "amd_clock_boost_fix.ico"
RUN_REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
RUN_REG_VALUE = "AMDClockBoostFix"
MUTEX_NAME = r"Global\AMDClockBoostFix_SingleInstance_Mutex"

for _search_dir in (str(BUNDLE_ROOT), str(BASE)):
    if _search_dir not in sys.path:
        sys.path.insert(0, _search_dir)

# Hidden import explícito apenas para análise estática do PyInstaller (nunca executado na UI)
if False:  # pragma: no cover
    from adlx import ADLX  # noqa: F401


def app_icon_path() -> Path:
    """Locate the bundled app icon in source and PyInstaller builds."""
    return BUNDLE_ROOT / ICON_RELATIVE_PATH


# Referências fixas (não são valores de overclock escolhidos pelo usuário).
# Adicione novos modelos somente após confirmar ID PCI e clock boost de referência.
GPU_PROFILES: dict[str, dict[str, Any]] = {
    "RX 550": {"series": "RX 500", "reference_boost_mhz": 1183},
    "RX 560": {"series": "RX 500", "reference_boost_mhz": 1275},
    "RX 570": {"series": "RX 500", "reference_boost_mhz": 1244},
    "RX 580": {"series": "RX 500", "reference_boost_mhz": 1340},
    "RX 590": {"series": "RX 500", "reference_boost_mhz": 1545},
    "RX 580 2048SP": {"series": "RX 500", "reference_boost_mhz": 1284},
    "RX 6400": {"series": "RX 6000", "reference_boost_mhz": 2321},
    "RX 6500 XT": {"series": "RX 6000", "reference_boost_mhz": 2815},
    "RX 6600": {"series": "RX 6000", "reference_boost_mhz": 2491},
    "RX 6600 XT": {"series": "RX 6000", "reference_boost_mhz": 2589},
    "RX 6650 XT": {"series": "RX 6000", "reference_boost_mhz": 2635},
    "RX 6700": {"series": "RX 6000", "reference_boost_mhz": 2450},
    "RX 6700 XT": {"series": "RX 6000", "reference_boost_mhz": 2581},
    "RX 6750 XT": {"series": "RX 6000", "reference_boost_mhz": 2600},
    "RX 6800": {"series": "RX 6000", "reference_boost_mhz": 2105},
    "RX 6800 XT": {"series": "RX 6000", "reference_boost_mhz": 2250},
    "RX 6900 XT": {"series": "RX 6000", "reference_boost_mhz": 2250},
    "RX 6950 XT": {"series": "RX 6000", "reference_boost_mhz": 2310},
    "RX 7400": {"series": "RX 7000", "reference_boost_mhz": 1100},
    "RX 7600": {"series": "RX 7000", "reference_boost_mhz": 2655},
    "RX 7650 GRE": {"series": "RX 7000", "reference_boost_mhz": 2695},
    "RX 7600 XT": {"series": "RX 7000", "reference_boost_mhz": 2755},
    "RX 7700": {"series": "RX 7000", "reference_boost_mhz": 2459},
    "RX 7700 XT": {"series": "RX 7000", "reference_boost_mhz": 2544},
    "RX 7800 XT": {"series": "RX 7000", "reference_boost_mhz": 2430},
    "RX 7900 GRE": {"series": "RX 7000", "reference_boost_mhz": 2245},
    "RX 7900 XT": {"series": "RX 7000", "reference_boost_mhz": 2400},
    "RX 7900 XTX": {"series": "RX 7000", "reference_boost_mhz": 2500},
}


def normalize_gpu_name(name: str) -> str:
    normalized = re.sub(r"[^a-z0-9]", "", str(name).casefold())
    for prefix in ("amdradeon", "radeon", "amd"):
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix):]
            break
    return normalized.replace("graphics", "").replace("series", "")


def profile_for_gpu_name(name: str) -> str | None:
    normalized = normalize_gpu_name(name)
    return next((model for model in GPU_PROFILES if normalized == normalize_gpu_name(model)), None)


def appdata() -> Path:
    p = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local")) / APP
    p.mkdir(parents=True, exist_ok=True)
    return p


def settings_file() -> Path:
    return appdata() / "settings.json"


def read_settings() -> dict[str, Any]:
    try:
        data = json.loads(settings_file().read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError, json.JSONDecodeError):
        return {}


def write_settings(data: dict[str, Any]) -> None:
    path = settings_file()
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def legacy_startup_link_path() -> Path | None:
    roaming = os.environ.get("APPDATA")
    if not roaming:
        return None
    return Path(roaming) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup" / "AMD Clock Boost Fix.lnk"


def remove_legacy_startup_shortcut() -> None:
    link = legacy_startup_link_path()
    if link is not None:
        try:
            link.unlink()
        except OSError:
            pass


def build_startup_command() -> str:
    if getattr(sys, "frozen", False):
        target = str(Path(sys.executable).resolve())
        return f'"{target}" --startup-apply'
    target = str(Path(sys.executable).resolve())
    script = str(Path(__file__).resolve())
    return f'"{target}" "{script}" --startup-apply'


def is_startup_enabled() -> bool:
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_REG_PATH, 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, RUN_REG_VALUE)
            return bool(value)
    except OSError:
        return False


def enable_startup_entry() -> str:
    command = build_startup_command()
    with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, RUN_REG_PATH, 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, RUN_REG_VALUE, 0, winreg.REG_SZ, command)
    remove_legacy_startup_shortcut()
    return command


def disable_startup_entry() -> None:
    remove_legacy_startup_shortcut()
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_REG_PATH, 0, winreg.KEY_SET_VALUE) as key:
            winreg.DeleteValue(key, RUN_REG_VALUE)
    except FileNotFoundError:
        pass


def acquire_single_instance_mutex(name: str = MUTEX_NAME) -> tuple[bool, int | None]:
    """Acquire a named Windows Mutex to prevent concurrent instances."""
    if os.name != "nt":
        return True, None
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateMutexW.argtypes = [ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p]
    kernel32.CreateMutexW.restype = ctypes.c_void_p
    handle = kernel32.CreateMutexW(None, False, name)
    if not handle:
        return True, None
    error_already_exists = 183
    if ctypes.get_last_error() == error_already_exists:
        kernel32.CloseHandle(handle)
        return False, None
    return True, int(handle)


def release_single_instance_mutex(handle: int | None) -> None:
    if handle and os.name == "nt":
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.CloseHandle(ctypes.c_void_p(handle))


def apply_saved_startup_profile() -> dict[str, Any]:
    settings_exist = settings_file().exists()
    saved = read_settings()
    if settings_exist and not saved.get("startup_enabled"):
        return {"ok": False, "error": "A reaplicação automática está desativada no perfil salvo."}
    has_saved_profile = bool(saved.get("profile_name"))
    profile = saved.get("profile_name")
    reference = saved.get("reference_boost_mhz")
    expected_gpu = saved.get("gpu_name")
    if settings_exist and (not has_saved_profile or not expected_gpu):
        return {"ok": False, "error": "O perfil salvo está incompleto; abra o programa e aplique novamente."}
    if has_saved_profile:
        if profile not in GPU_PROFILES:
            return {"ok": False, "error": "O perfil salvo não está na base de GPUs."}
        try:
            reference = int(reference)
        except (TypeError, ValueError):
            return {"ok": False, "error": "O clock salvo é inválido; abra o programa e aplique novamente."}
        if reference != GPU_PROFILES[profile]["reference_boost_mhz"]:
            return {"ok": False, "error": "O clock salvo não corresponde à referência oficial do perfil."}

    checked: dict[str, Any] | None = None
    for attempt in range(8):
        checked = run_worker("check")
        if checked.get("ok"):
            break
        if attempt < 7:
            time.sleep(3)
    if not checked or not checked.get("ok"):
        return checked or {"ok": False, "error": "Não foi possível consultar o driver AMD após o login."}

    adapters = checked.get("adapters", [])
    if has_saved_profile:
        matches = [
            adapter for adapter in adapters
            if adapter.get("gpu") == expected_gpu and adapter.get("profile_name") == profile
        ]
        if len(matches) != 1:
            return {"ok": False, "error": "A GPU atual não corresponde de forma única ao perfil salvo; nenhuma alteração foi feita."}
        adapter = matches[0]
    else:
        candidates: dict[str, list[dict[str, Any]]] = {}
        for adapter in adapters:
            model = adapter.get("profile_name")
            if not model or not adapter.get("supported"):
                continue
            target = GPU_PROFILES[model]["reference_boost_mhz"]
            if adapter["minimum_mhz"] <= target <= adapter["maximum_mhz"]:
                candidates.setdefault(model, []).append(adapter)
        unique = [(model, matches[0]) for model, matches in candidates.items() if len(matches) == 1]
        if len(unique) != 1:
            return {"ok": False, "error": "Não foi encontrada exatamente uma GPU com perfil seguro; nenhuma alteração foi feita."}
        profile, adapter = unique[0]
        reference = GPU_PROFILES[profile]["reference_boost_mhz"]
        expected_gpu = adapter["gpu"]

    if not adapter.get("supported") or not adapter["minimum_mhz"] <= reference <= adapter["maximum_mhz"]:
        return {"ok": False, "error": "O ajuste não é suportado ou está fora da faixa atual do driver; nenhuma alteração foi feita."}
    result = run_worker("apply", profile)
    if result.get("ok"):
        result["startup_gpu"] = expected_gpu
        settings = {
            "profile_name": profile,
            "gpu_name": expected_gpu,
            "reference_boost_mhz": reference,
            "startup_enabled": True,
        }
        try:
            write_settings(settings)
        except OSError as exc:
            result["warning"] = f"O clock foi aplicado, mas o perfil local não pôde ser salvo: {exc}"
    return result


def write_startup_log(result: dict[str, Any]) -> None:
    record = {
        "version": APP_VERSION,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "ok": bool(result.get("ok")),
        "gpu": result.get("gpu") or result.get("startup_gpu"),
        "profile": result.get("profile_name"),
        "applied_mhz": result.get("applied_mhz"),
        "error": result.get("error"),
        "warning": result.get("warning"),
    }
    log_path = appdata() / "startup.log"
    log_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")


def cleanup_legacy_restart_confirmation() -> None:
    """Remove apenas o RunOnce e o estado pendente criados pelo RX7600 Clock Helper 1.6."""
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
            0,
            winreg.KEY_SET_VALUE,
        ) as key:
            winreg.DeleteValue(key, LEGACY_APP + "Confirm")
    except OSError:
        pass
    old_pending = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local")) / LEGACY_APP / "pending_restart.json"
    try:
        old_pending.unlink()
    except OSError:
        pass


def validate_result_file_path(path: str | Path) -> Path:
    """Ensure worker output path stays strictly inside the application AppData folder."""
    allowed_dir = appdata().resolve()
    target = Path(path).resolve()
    if target.parent != allowed_dir or target.suffix.lower() != ".json":
        raise ValueError("Caminho de arquivo de resultado fora do diretório permitido.")
    return target


def write_worker_result(path: str | Path | None, data: dict[str, Any]) -> None:
    encoded = json.dumps(data, ensure_ascii=False)
    if path:
        safe_path = validate_result_file_path(path)
        safe_path.write_text(encoded, encoding="utf-8")
    elif sys.stdout is not None:
        print(encoded, flush=True)


def read_gpu_info(gpu: Any, tuning: Any) -> dict[str, Any]:
    manual = None
    try:
        profile_name = profile_for_gpu_name(gpu.Name())
        if not tuning.IsSupportedManualGFXTuning(gpu):
            return {
                "gpu": gpu.Name(),
                "profile_name": profile_name,
                "supported": False,
                "error": "Ajuste manual não suportado pelo driver.",
            }
        manual = tuning.GetManualGFXTuning2(gpu)
        if manual is None:
            return {
                "gpu": gpu.Name(),
                "profile_name": profile_name,
                "supported": False,
                "error": "Interface ADLX indisponível.",
            }
        limits = manual.GetGPUMaxFrequencyRange()
        profile_clock = GPU_PROFILES[profile_name]["reference_boost_mhz"] if profile_name else None
        return {
            "gpu": gpu.Name(),
            "profile_name": profile_name,
            "reference_boost_mhz": profile_clock,
            "current_mhz": int(manual.GetGPUMaxFrequency()),
            "default_mhz": int(manual.GetGPUMaxFrequencyDefault()),
            "minimum_mhz": int(limits["min_value"]),
            "maximum_mhz": int(limits["max_value"]),
            "supported": True,
        }
    finally:
        manual = None
        gc.collect()


def _apply_frequency(
    gpu: Any,
    tuning: Any,
    profile_id: str,
    info: dict[str, Any],
    target_mhz: int,
    ADLX: Any,
    *,
    is_restore: bool = False,
) -> tuple[dict[str, Any], int]:
    if not info["minimum_mhz"] <= target_mhz <= info["maximum_mhz"]:
        label = (
            f"O padrão do driver ({target_mhz} MHz) está fora da faixa atual."
            if is_restore
            else f"{target_mhz} MHz está fora da faixa do driver ({info['minimum_mhz']}–{info['maximum_mhz']} MHz)."
        )
        return {"ok": False, "error": label, **info}, 8

    manual = None
    try:
        manual = tuning.GetManualGFXTuning2(gpu)
        if manual is None:
            action = "restaurar o padrão" if is_restore else "aplicar o perfil"
            return {"ok": False, "error": f"Interface ADLX indisponível para {action}.", **info}, 9
        result = manual.SetGPUMaxFrequency(target_mhz)
        readback = int(manual.GetGPUMaxFrequency())
    finally:
        manual = None
        gc.collect()

    if result != ADLX.ADLX_RESULT.ADLX_OK or readback != target_mhz:
        action = "a restauração para" if is_restore else ""
        prefix = f"O driver não confirmou {action} {target_mhz} MHz".replace("  ", " ")
        return {
            "ok": False,
            "error": f"{prefix} (leitura: {readback} MHz).",
            "current_mhz": readback,
            **info,
        }, 10

    payload: dict[str, Any] = {
        "ok": True,
        "applied_mhz": readback,
        **info,
        "profile_name": profile_id,
    }
    if is_restore:
        payload["restored_default_mhz"] = target_mhz
    else:
        payload["reference_boost_mhz"] = target_mhz
    return payload, 0


def _run_adlx_operation(mode: str, profile_id: str | None) -> tuple[dict[str, Any], int]:
    from adlx import ADLX

    helper = ADLX.ADLXHelper()
    if helper.Initialize() != ADLX.ADLX_RESULT.ADLX_OK:
        return {"ok": False, "error": "ADLX não inicializou. Confira o driver AMD."}, 2

    services = tuning = gpu = gpu_list = amd_gpus = matches = None
    payload: dict[str, Any] = {"ok": False, "error": "O worker ADLX não concluiu a operação."}
    exit_code = 1
    try:
        services = helper.GetSystemServices()
        tuning = services.GetGPUTuningServices()
        gpu_list = services.GetGPUs()
        amd_gpus = [item for item in gpu_list if item.VendorId() == "1002"]

        if mode == "check":
            adapters = [read_gpu_info(item, tuning) for item in amd_gpus]
            if not adapters:
                payload, exit_code = {"ok": False, "error": "Nenhuma GPU AMD foi detectada."}, 3
            else:
                payload, exit_code = {"ok": True, "adapters": adapters}, 0
        elif profile_id not in GPU_PROFILES:
            payload, exit_code = {"ok": False, "error": "Perfil de GPU inválido."}, 4
        else:
            matches = [item for item in amd_gpus if profile_for_gpu_name(item.Name()) == profile_id]
            if len(matches) == 0:
                payload, exit_code = {
                    "ok": False,
                    "error": f"A GPU selecionada ({profile_id}) não foi encontrada entre as GPUs detectadas.",
                }, 5
            elif len(matches) > 1:
                payload, exit_code = {
                    "ok": False,
                    "error": (
                        f"Foram detectadas {len(matches)} GPUs com o nome {profile_id}. "
                        "A aplicação foi bloqueada porque não é possível distingui-las com segurança."
                    ),
                }, 6
            else:
                gpu = matches[0]
                info = read_gpu_info(gpu, tuning)
                if not info.get("supported"):
                    payload, exit_code = {"ok": False, "error": info.get("error", "Ajuste não suportado."), **info}, 7
                elif mode == "restore":
                    payload, exit_code = _apply_frequency(
                        gpu, tuning, profile_id, info, int(info["default_mhz"]), ADLX, is_restore=True
                    )
                else:
                    target_mhz = int(GPU_PROFILES[profile_id]["reference_boost_mhz"])
                    payload, exit_code = _apply_frequency(
                        gpu, tuning, profile_id, info, target_mhz, ADLX, is_restore=False
                    )
    finally:
        # Libera todas as interfaces filhas antes de chamar helper.Terminate() para evitar 0xC0000005
        gpu = tuning = services = gpu_list = amd_gpus = matches = None
        gc.collect()
        term = helper.Terminate()
        helper = None
        gc.collect()
        if term != ADLX.ADLX_RESULT.ADLX_OK and payload.get("ok"):
            payload = {"ok": False, "error": f"ADLX não encerrou corretamente: {term}"}
            exit_code = 12

    return payload, exit_code


def worker(mode: str, profile_id: str | None = None, result_file: str | None = None) -> int:
    payload: dict[str, Any] = {"ok": False, "error": "O worker ADLX não concluiu a operação."}
    exit_code = 1
    try:
        payload, exit_code = _run_adlx_operation(mode, profile_id)
    except Exception as e:
        payload = {"ok": False, "error": f"Erro ADLX: {type(e).__name__}: {e}"}
        exit_code = 11

    try:
        write_worker_result(result_file, payload)
    except Exception:
        exit_code = 13
    return exit_code


def run_worker(mode: str, profile_id: str | None = None) -> dict[str, Any]:
    if getattr(sys, "frozen", False):
        cmd = [str(Path(sys.executable).resolve()), "--worker", mode]
    else:
        cmd = [sys.executable, str(Path(__file__).resolve()), "--worker", mode]
    if profile_id:
        cmd.extend(["--profile", profile_id])
    result_path = appdata() / f"worker-{os.getpid()}-{threading.get_ident()}-{time.time_ns()}.json"
    cmd.extend(["--result-file", str(result_path)])
    try:
        p = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        if result_path.exists():
            data = json.loads(result_path.read_text(encoding="utf-8"))
            if p.returncode != 0:
                if not data.get("ok") and data.get("error"):
                    data["error"] += f" (worker: código {p.returncode})"
                    return data
                return {
                    "ok": False,
                    "error": f"O worker encerrou com código {p.returncode}; operação não considerada confirmada.",
                    "details": data,
                }
            return data
        return {"ok": False, "error": p.stderr.strip() or f"Worker terminou sem resultado (código {p.returncode})."}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "A comunicação com o driver excedeu 60 segundos; o valor não foi confirmado."}
    except (OSError, ValueError, json.JSONDecodeError) as e:
        return {"ok": False, "error": f"Falha ao consultar o worker: {e}"}
    finally:
        try:
            result_path.unlink()
        except OSError:
            pass


class UI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("AMD Clock Boost Fix")
        try:
            root.iconbitmap(default=str(app_icon_path()))
        except (OSError, tk.TclError):
            pass
        root.geometry("700x500")
        root.minsize(620, 450)
        root.resizable(True, True)
        self.status = tk.StringVar(value="Consultando GPUs AMD e o driver…")
        self.summary = tk.StringVar(value="Aguardando identificação…")
        self.current = tk.StringVar(value="")
        self.range_info = tk.StringVar(value="")
        self.detected_profile: str | None = None
        self.busy = False
        self.settings = read_settings()
        legacy_link = legacy_startup_link_path()
        if is_startup_enabled() or (legacy_link is not None and legacy_link.exists()):
            self.settings["startup_enabled"] = True
        self.autostart_var = tk.BooleanVar(value=bool(self.settings.get("startup_enabled")))

        frame = ttk.Frame(root, padding=20)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="AMD Clock Boost Fix", font=("Segoe UI", 15, "bold")).pack(anchor="w")
        ttk.Label(frame, text="GPU identificada", font=("Segoe UI", 10)).pack(anchor="w", pady=(16, 2))
        ttk.Label(frame, textvariable=self.summary, wraplength=620, font=("Segoe UI", 17, "bold")).pack(anchor="w", pady=(0, 8))
        ttk.Label(frame, textvariable=self.current, wraplength=620, justify="left").pack(anchor="w", pady=(0, 4))
        ttk.Label(frame, textvariable=self.range_info, wraplength=620, justify="left").pack(anchor="w", pady=(0, 12))
        self.apply_button = ttk.Button(
            frame, text="Aplicar referência da GPU", command=lambda: self.run("apply"), state="disabled"
        )
        self.apply_button.pack(anchor="w", pady=(0, 6))
        self.restore_button = ttk.Button(
            frame, text="Restaurar clock boost original", command=lambda: self.run("restore"), state="disabled"
        )
        self.restore_button.pack(anchor="w", pady=(0, 8))
        self.startup_check = ttk.Checkbutton(
            frame,
            text="Reaplicar automaticamente ao entrar no Windows",
            variable=self.autostart_var,
            command=self.toggle_autostart,
            state="disabled",
        )
        self.startup_check.pack(anchor="w", pady=(0, 4))
        self.progress = ttk.Progressbar(frame, mode="indeterminate")
        self.progress.pack(fill="x", pady=(12, 6))
        ttk.Label(frame, textvariable=self.status, wraplength=620, justify="left").pack(fill="x", anchor="w")
        ttk.Label(
            frame,
            text="O aplicativo reaplica o limite após o login. O clock instantâneo varia com carga e temperatura.",
            wraplength=620,
            justify="left",
        ).pack(fill="x", anchor="w", pady=(8, 0))

        self.root.after(150, lambda: self.run("check"))
        self.update_control_states()

    def update_control_states(self) -> None:
        button_state = "normal" if not self.busy and self.detected_profile else "disabled"
        self.apply_button.configure(state=button_state)
        self.restore_button.configure(state=button_state)
        can_toggle = bool(self.settings.get("profile_name")) and not self.busy
        self.startup_check.configure(state="normal" if can_toggle else "disabled")

    def toggle_autostart(self) -> None:
        enabled = bool(self.autostart_var.get())
        previous = bool(self.settings.get("startup_enabled"))
        if enabled and not self.settings.get("profile_name"):
            self.autostart_var.set(False)
            messagebox.showinfo("Aplique primeiro", "Aplique uma referência uma vez antes de ativar a reaplicação automática.")
            return
        updated = dict(self.settings)
        updated["startup_enabled"] = enabled
        try:
            if enabled:
                write_settings(updated)
                enable_startup_entry()
                self.status.set("Reaplicação automática ativada para o próximo login.")
            else:
                disable_startup_entry()
                write_settings(updated)
                self.status.set("Reaplicação automática desativada.")
            self.settings = updated
        except Exception as exc:
            self.autostart_var.set(previous)
            rollback = dict(self.settings)
            rollback["startup_enabled"] = previous
            try:
                write_settings(rollback)
            except OSError:
                pass
            try:
                if previous:
                    enable_startup_entry()
                else:
                    disable_startup_entry()
            except OSError:
                pass
            messagebox.showerror("Inicialização não alterada", f"Não foi possível atualizar a inicialização do Windows:\n{exc}")
        self.update_control_states()

    def run(self, mode: str) -> None:
        if self.busy:
            return
        profile_id = self.detected_profile if mode in ("apply", "restore") else None
        if mode in ("apply", "restore") and profile_id not in GPU_PROFILES:
            messagebox.showerror("GPU indisponível", "Não há uma única GPU compatível identificada para esta ação.")
            return
        if mode == "restore" and not messagebox.askyesno(
            "Restaurar clock original",
            "O programa vai restaurar o clock boost padrão reportado pelo driver AMD e desativar a reaplicação automática no login. Deseja continuar?",
        ):
            return
        self.busy = True
        self.update_control_states()
        if mode == "check":
            self.status.set("Consultando as GPUs AMD…")
        elif mode == "restore":
            self.status.set(f"Validando a GPU e restaurando o clock padrão do driver para {profile_id}…")
        else:
            self.status.set(f"Validando novamente a GPU e aplicando a referência de {profile_id}…")
        self.progress.start(12)
        threading.Thread(target=self.work, args=(mode, profile_id), daemon=True).start()

    def work(self, mode: str, profile_id: str | None = None) -> None:
        result = run_worker(mode, profile_id)
        try:
            self.root.after(0, self.done, mode, profile_id, result)
        except tk.TclError:
            pass

    def done(self, mode: str, profile_id: str | None, result: dict[str, Any]) -> None:
        self.progress.stop()
        self.busy = False
        if not result.get("ok"):
            self.status.set(result.get("error", "Falha sem detalhe."))
            if mode == "check":
                self.detected_profile = None
                self.summary.set("Não foi possível identificar a GPU")
                self.current.set("")
                self.range_info.set("")
            if mode in ("apply", "restore"):
                messagebox.showerror("Clock não alterado", self.status.get())
            self.update_control_states()
            return
        if mode == "check":
            adapters = result.get("adapters", [])
            eligible_adapters: dict[str, list[dict[str, Any]]] = {}
            names = []
            for adapter in adapters:
                model = adapter.get("profile_name")
                if model and adapter.get("supported"):
                    reference = GPU_PROFILES[model]["reference_boost_mhz"]
                    if adapter["minimum_mhz"] <= reference <= adapter["maximum_mhz"]:
                        eligible_adapters.setdefault(model, []).append(adapter)
                names.append(adapter["gpu"])
            eligible_models = [model for model, matches in eligible_adapters.items() if len(matches) == 1]
            self.detected_profile = eligible_models[0] if len(eligible_models) == 1 else None
            self.summary.set("\n".join(names) if names else "Nenhuma GPU AMD foi encontrada")
            if self.detected_profile:
                adapter = eligible_adapters[self.detected_profile][0]
                reference = GPU_PROFILES[self.detected_profile]["reference_boost_mhz"]
                self.current.set(
                    f"Limite atual: {adapter['current_mhz']} MHz  |  Original da GPU: {adapter['default_mhz']} MHz  |  Referência: {reference} MHz"
                )
                self.range_info.set("GPU reconhecida e compatível. O modelo será validado novamente ao aplicar.")
                self.status.set("GPU pronta para aplicação da referência.")
            elif len(eligible_models) > 1:
                self.current.set("")
                self.range_info.set("Mais de uma GPU compatível foi encontrada. Aplicação bloqueada por segurança.")
                self.status.set("Não é possível escolher automaticamente entre várias GPUs compatíveis.")
            else:
                self.current.set("")
                self.range_info.set("O modelo não está na base, o ajuste não é suportado ou o clock está fora da faixa do driver.")
                self.status.set("Nenhum perfil compatível pode ser aplicado com segurança nesta máquina.")
            self.update_control_states()
            return

        applied = result["applied_mhz"]
        gpu_name = result.get("gpu") or result.get("startup_gpu") or "GPU identificada"
        self.summary.set(gpu_name)
        self.current.set(f"Limite atual: {applied} MHz  |  Referência aplicada: {applied} MHz")
        self.status.set(f"O driver confirmou a leitura de retorno em {applied} MHz.")
        if mode == "restore":
            profile = result["profile_name"]
            self.settings = {
                "profile_name": profile,
                "gpu_name": result["gpu"],
                "reference_boost_mhz": GPU_PROFILES[profile]["reference_boost_mhz"],
                "startup_enabled": False,
            }
            warnings = []
            self.autostart_var.set(False)
            try:
                disable_startup_entry()
            except OSError as exc:
                warnings.append(f"registro de inicialização: {exc}")
            try:
                write_settings(self.settings)
            except OSError as exc:
                warnings.append(f"configuração local: {exc}")
            self.current.set(f"Limite atual: {applied} MHz  |  Clock original restaurado: {applied} MHz")
            if warnings:
                detail = "\n".join(warnings)
                self.status.set("Clock original restaurado; houve um problema ao desativar a reaplicação automática.")
                messagebox.showwarning(
                    "Clock restaurado com aviso",
                    f"O driver confirmou o valor original de {applied} MHz, mas não foi possível concluir a desativação da reaplicação automática:\n{detail}",
                )
            else:
                self.status.set(f"Clock boost original restaurado e confirmado pelo driver: {applied} MHz.")
                messagebox.showinfo(
                    "Clock original restaurado",
                    f"{profile}: o clock boost original de {applied} MHz foi restaurado e confirmado pelo driver. A reaplicação automática foi desativada.",
                )
            self.update_control_states()
            return

        self.settings = {
            "profile_name": result["profile_name"],
            "gpu_name": result["gpu"],
            "reference_boost_mhz": applied,
            "startup_enabled": bool(self.autostart_var.get()),
        }
        try:
            write_settings(self.settings)
            if self.settings["startup_enabled"]:
                enable_startup_entry()
        except OSError as exc:
            self.status.set(f"Clock aplicado, mas não foi possível salvar/atualizar a inicialização: {exc}")
        self.update_control_states()
        messagebox.showinfo(
            "Aplicação confirmada",
            f"{result['profile_name']}: referência de {applied} MHz aplicada à GPU detectada e confirmada pelo driver.",
        )


def main() -> int:
    parser = argparse.ArgumentParser(prog=APP)
    parser.add_argument("--version", action="version", version=f"%(prog)s {APP_VERSION}")
    parser.add_argument("--worker", choices=("check", "apply", "restore"))
    parser.add_argument("--profile", choices=tuple(GPU_PROFILES))
    parser.add_argument("--result-file")
    parser.add_argument("--startup-apply", action="store_true")
    args = parser.parse_args()

    if args.worker:
        return worker(args.worker, args.profile, args.result_file)

    acquired, mutex_handle = acquire_single_instance_mutex()
    if not acquired:
        if not args.startup_apply:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo(
                "AMD Clock Boost Fix",
                "O AMD Clock Boost Fix já está em execução.",
            )
            root.destroy()
        return 0

    try:
        cleanup_legacy_restart_confirmation()
        if args.startup_apply:
            time.sleep(4)
            result = apply_saved_startup_profile()
            try:
                write_startup_log(result)
            except OSError:
                pass
            return 0 if result.get("ok") else 1
        root = tk.Tk()
        UI(root)
        root.mainloop()
        return 0
    finally:
        release_single_instance_mutex(mutex_handle)


if __name__ == "__main__":
    raise SystemExit(main())
