# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMD Clock Boost Fix contributors
from __future__ import annotations
import argparse, ctypes, gc, json, os, re, subprocess, sys, threading, time, tkinter as tk, uuid, winreg
from pathlib import Path
from tkinter import messagebox, ttk

APP = "AMDClockBoostFix"
LEGACY_APP = "RX7600ClockHelper"
BASE = Path(__file__).resolve().parent
ICON_RELATIVE_PATH = Path("assets") / "amd_clock_boost_fix.ico"

def app_icon_path():
    """Locate the bundled app icon in source and PyInstaller builds."""
    bundle_root = Path(getattr(sys, "_MEIPASS", BASE))
    return bundle_root / ICON_RELATIVE_PATH

# Referências fixas (não são valores de overclock escolhidos pelo usuário).
# Adicione novos modelos somente após confirmar ID PCI e clock boost de referência.
GPU_PROFILES = {
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

def normalize_gpu_name(name):
    normalized = re.sub(r"[^a-z0-9]", "", str(name).casefold())
    for prefix in ("amdradeon", "radeon", "amd"):
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix):]
            break
    return normalized.replace("graphics", "").replace("series", "")

def profile_for_gpu_name(name):
    normalized = normalize_gpu_name(name)
    return next((model for model in GPU_PROFILES if normalized == normalize_gpu_name(model)), None)

def appdata():
    p = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local")) / APP
    p.mkdir(parents=True, exist_ok=True)
    return p

def settings_file():
    return appdata() / "settings.json"

def read_settings():
    try:
        data = json.loads(settings_file().read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError, json.JSONDecodeError):
        return {}

def write_settings(data):
    path = settings_file()
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)

def startup_link_path():
    roaming = os.environ.get("APPDATA")
    if not roaming:
        raise OSError("A pasta AppData do usuário não está disponível.")
    folder = Path(roaming) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "AMD Clock Boost Fix.lnk"

class _GUID(ctypes.Structure):
    _fields_ = [("Data1", ctypes.c_uint32), ("Data2", ctypes.c_uint16),
                ("Data3", ctypes.c_uint16), ("Data4", ctypes.c_ubyte * 8)]

def _guid(value):
    raw = uuid.UUID(value).bytes_le
    result = _GUID()
    ctypes.memmove(ctypes.byref(result), raw, 16)
    return result

def create_startup_shortcut():
    link_path = startup_link_path()
    if getattr(sys, "frozen", False):
        target = str(Path(sys.executable).resolve())
        arguments = "--startup-apply --silent"
        working_dir = str(Path(target).parent)
    else:
        target = str(Path(sys.executable).resolve())
        script = str(Path(__file__).resolve())
        arguments = f'"{script}" --startup-apply'
        working_dir = str(Path(script).parent)

    ole32 = ctypes.WinDLL("ole32")
    ole32.CoInitialize.argtypes = [ctypes.c_void_p]
    ole32.CoInitialize.restype = ctypes.c_long
    ole32.CoCreateInstance.argtypes = [ctypes.POINTER(_GUID), ctypes.c_void_p, ctypes.c_uint32,
                                       ctypes.POINTER(_GUID), ctypes.POINTER(ctypes.c_void_p)]
    ole32.CoCreateInstance.restype = ctypes.c_long
    ole32.CoUninitialize.argtypes = []
    ole32.CoUninitialize.restype = None
    init_result = ole32.CoInitialize(None)
    initialized_here = init_result >= 0
    clsid_shell_link = _guid("00021401-0000-0000-C000-000000000046")
    iid_shell_link = _guid("000214F9-0000-0000-C000-000000000046")
    iid_persist_file = _guid("0000010B-0000-0000-C000-000000000046")
    shell_link = ctypes.c_void_p()
    persist = ctypes.c_void_p()
    hr = ole32.CoCreateInstance(ctypes.byref(clsid_shell_link), None, 1,
                                ctypes.byref(iid_shell_link), ctypes.byref(shell_link))
    if hr < 0:
        if initialized_here: ole32.CoUninitialize()
        raise OSError(f"Não foi possível criar atalho do Windows (HRESULT 0x{hr & 0xffffffff:08X}).")

    def method(pointer, index, restype, *argtypes):
        table = ctypes.cast(pointer, ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))).contents
        return ctypes.WINFUNCTYPE(restype, ctypes.c_void_p, *argtypes)(table[index])

    try:
        for index, value in ((20, target), (11, arguments), (9, working_dir),
                             (7, "AMD Clock Boost Fix — reaplicar referência ao entrar no Windows")):
            hr = method(shell_link, index, ctypes.c_long, ctypes.c_wchar_p)(shell_link, value)
            if hr < 0:
                raise OSError(f"Falha ao montar o atalho do Windows (HRESULT 0x{hr & 0xffffffff:08X}).")
        query = method(shell_link, 0, ctypes.c_long, ctypes.POINTER(_GUID), ctypes.POINTER(ctypes.c_void_p))
        hr = query(shell_link, ctypes.byref(iid_persist_file), ctypes.byref(persist))
        if hr < 0:
            raise OSError(f"Não foi possível preparar o atalho do Windows (HRESULT 0x{hr & 0xffffffff:08X}).")
        hr = method(persist, 6, ctypes.c_long, ctypes.c_wchar_p, ctypes.c_int)(persist, str(link_path), 1)
        if hr < 0:
            raise OSError(f"Não foi possível salvar o atalho na pasta Inicializar (HRESULT 0x{hr & 0xffffffff:08X}).")
    finally:
        if persist:
            method(persist, 2, ctypes.c_ulong)(persist)
        if shell_link:
            method(shell_link, 2, ctypes.c_ulong)(shell_link)
        if initialized_here:
            ole32.CoUninitialize()
    return link_path

def remove_startup_shortcut():
    link = startup_link_path()
    try:
        link.unlink()
    except FileNotFoundError:
        pass
    return link

def apply_saved_startup_profile():
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

    checked = None
    for attempt in range(5):
        checked = run_worker("check")
        if checked.get("ok"):
            break
        if attempt < 4:
            time.sleep(5)
    if not checked or not checked.get("ok"):
        return checked or {"ok": False, "error": "Não foi possível consultar o driver AMD após o login."}

    adapters = checked.get("adapters", [])
    if has_saved_profile:
        matches = [adapter for adapter in adapters
                   if adapter.get("gpu") == expected_gpu and adapter.get("profile_name") == profile]
        if len(matches) != 1:
            return {"ok": False, "error": "A GPU atual não corresponde de forma única ao perfil salvo; nenhuma alteração foi feita."}
        adapter = matches[0]
    else:
        candidates = {}
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

def write_startup_log(result):
    record = {
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

def cleanup_legacy_restart_confirmation():
    # Remove apenas o RunOnce e o estado pendente criados pelo RX7600 Clock Helper 1.6.
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
                            0, winreg.KEY_SET_VALUE) as key:
            winreg.DeleteValue(key, LEGACY_APP + "Confirm")
    except OSError:
        pass
    old_pending = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local")) / LEGACY_APP / "pending_restart.json"
    try: old_pending.unlink()
    except FileNotFoundError: pass
    except OSError: pass

def write_worker_result(path, data):
    encoded = json.dumps(data, ensure_ascii=False)
    if path:
        Path(path).write_text(encoded, encoding="utf-8")
    elif sys.stdout is not None:
        print(encoded, flush=True)

def read_gpu_info(gpu, tuning):
    manual = None
    try:
        if not tuning.IsSupportedManualGFXTuning(gpu):
            return {"gpu": gpu.Name(), "profile_name": profile_for_gpu_name(gpu.Name()),
                    "supported": False, "error": "Ajuste manual não suportado pelo driver."}
        manual = tuning.GetManualGFXTuning2(gpu)
        if manual is None:
            return {"gpu": gpu.Name(), "profile_name": profile_for_gpu_name(gpu.Name()),
                    "supported": False, "error": "Interface ADLX indisponível."}
        limits = manual.GetGPUMaxFrequencyRange()
        profile_name = profile_for_gpu_name(gpu.Name())
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

def worker(mode, profile_id=None, result_file=None):
    helper = None
    initialized = False
    services = tuning = gpu = gpu_list = amd_gpus = matches = None
    payload = {"ok": False, "error": "O worker ADLX não concluiu a operação."}
    exit_code = 1
    try:
        from adlx import ADLX
        helper = ADLX.ADLXHelper()
        if helper.Initialize() != ADLX.ADLX_RESULT.ADLX_OK:
            payload = {"ok": False, "error": "ADLX não inicializou. Confira o driver AMD."}
            exit_code = 2
        else:
            initialized = True
            services = helper.GetSystemServices()
            tuning = services.GetGPUTuningServices()
            gpu_list = services.GetGPUs()
            amd_gpus = [item for item in gpu_list if item.VendorId() == "1002"]
            if mode == "check":
                adapters = [read_gpu_info(item, tuning) for item in amd_gpus]
                if not adapters:
                    payload = {"ok": False, "error": "Nenhuma GPU AMD foi detectada."}
                    exit_code = 3
                else:
                    payload = {"ok": True, "adapters": adapters}
                    exit_code = 0
            elif mode == "restore":
                if profile_id not in GPU_PROFILES:
                    payload = {"ok": False, "error": "Perfil de GPU inválido."}
                    exit_code = 4
                else:
                    matches = [item for item in amd_gpus
                               if profile_for_gpu_name(item.Name()) == profile_id]
                    if len(matches) != 1:
                        payload = {"ok": False, "error":
                                   "A restauração exige uma única GPU compatível identificada; nenhuma alteração foi feita."}
                        exit_code = 5
                    else:
                        gpu = matches[0]
                        info = read_gpu_info(gpu, tuning)
                        if not info.get("supported"):
                            payload = {"ok": False, "error": info.get("error", "Ajuste não suportado."), **info}
                            exit_code = 7
                        else:
                            chosen = int(info["default_mhz"])
                            if not info["minimum_mhz"] <= chosen <= info["maximum_mhz"]:
                                payload = {"ok": False, "error":
                                           f"O padrão do driver ({chosen} MHz) está fora da faixa atual.", **info}
                                exit_code = 8
                            else:
                                manual = tuning.GetManualGFXTuning2(gpu)
                                if manual is None:
                                    payload = {"ok": False, "error": "Interface ADLX indisponível para restaurar o padrão.", **info}
                                    exit_code = 9
                                else:
                                    result = manual.SetGPUMaxFrequency(chosen)
                                    readback = int(manual.GetGPUMaxFrequency())
                                    manual = None
                                    gc.collect()
                                    if result != ADLX.ADLX_RESULT.ADLX_OK or readback != chosen:
                                        payload = {"ok": False, "error":
                                                   f"O driver não confirmou a restauração para {chosen} MHz (leitura: {readback} MHz).",
                                                   "current_mhz": readback, **info}
                                        exit_code = 10
                                    else:
                                        payload = {"ok": True, "applied_mhz": readback,
                                                   "restored_default_mhz": chosen, **info,
                                                   "profile_name": profile_id}
                                        exit_code = 0
            elif profile_id not in GPU_PROFILES:
                payload = {"ok": False, "error": "Perfil de GPU inválido."}
                exit_code = 4
            else:
                matches = [item for item in amd_gpus
                           if profile_for_gpu_name(item.Name()) == profile_id]
                if len(matches) == 0:
                    payload = {"ok": False, "error":
                               f"A GPU selecionada ({profile_id}) não foi encontrada entre as GPUs detectadas."}
                    exit_code = 5
                elif len(matches) > 1:
                    payload = {"ok": False, "error":
                               f"Foram detectadas {len(matches)} GPUs com o nome {profile_id}. "
                               "A aplicação foi bloqueada porque não é possível distingui-las com segurança."}
                    exit_code = 6
                else:
                    gpu = matches[0]
                    info = read_gpu_info(gpu, tuning)
                    if not info.get("supported"):
                        payload = {"ok": False, "error": info.get("error", "Ajuste não suportado."),
                                   **info}
                        exit_code = 7
                    else:
                        chosen = int(GPU_PROFILES[profile_id]["reference_boost_mhz"])
                        if not info["minimum_mhz"] <= chosen <= info["maximum_mhz"]:
                            payload = {"ok": False, "error":
                                       f"{chosen} MHz está fora da faixa do driver "
                                       f"({info['minimum_mhz']}–{info['maximum_mhz']} MHz).", **info}
                            exit_code = 8
                        else:
                            # Reacquire tuning interface for the unique, exactly matched GPU.
                            manual = tuning.GetManualGFXTuning2(gpu)
                            if manual is None:
                                payload = {"ok": False, "error": "Interface ADLX indisponível para aplicar o perfil.", **info}
                                exit_code = 9
                            else:
                                result = manual.SetGPUMaxFrequency(chosen)
                                readback = int(manual.GetGPUMaxFrequency())
                                manual = None
                                gc.collect()
                                if result != ADLX.ADLX_RESULT.ADLX_OK or readback != chosen:
                                    payload = {"ok": False, "error":
                                               f"O driver não confirmou {chosen} MHz (leitura: {readback} MHz).",
                                               "current_mhz": readback, **info}
                                    exit_code = 10
                                else:
                                    payload = {"ok": True, "applied_mhz": readback,
                                               **info, "reference_boost_mhz": chosen,
                                               "profile_name": profile_id}
                                    exit_code = 0
    except Exception as e:
        payload = {"ok": False, "error": f"Erro ADLX: {type(e).__name__}: {e}"}
        exit_code = 11
    finally:
        manual = gpu = tuning = services = gpu_list = amd_gpus = matches = None
        gc.collect()
        if helper is not None and initialized:
            try:
                from adlx import ADLX
                term = helper.Terminate()
                if term != ADLX.ADLX_RESULT.ADLX_OK and payload.get("ok"):
                    payload = {"ok": False, "error": f"ADLX não encerrou corretamente: {term}"}
                    exit_code = 12
            except Exception as e:
                payload = {"ok": False, "error": f"Falha ao encerrar ADLX: {e}"}
                exit_code = 12
    try:
        write_worker_result(result_file, payload)
    except Exception:
        exit_code = 13
    return exit_code

def run_worker(mode, profile_id=None):
    if getattr(sys, "frozen", False):
        cmd = [str(Path(sys.executable).resolve()), "--worker", mode]
    else:
        cmd = [sys.executable, str(Path(__file__).resolve()), "--worker", mode]
    if profile_id:
        cmd.extend(["--profile", profile_id])
    result_path = appdata() / f"worker-{os.getpid()}-{threading.get_ident()}-{time.time_ns()}.json"
    cmd.extend(["--result-file", str(result_path)])
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=60, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        if result_path.exists():
            data = json.loads(result_path.read_text(encoding="utf-8"))
            if p.returncode != 0:
                if not data.get("ok") and data.get("error"):
                    data["error"] += f" (worker: código {p.returncode})"
                    return data
                return {"ok": False, "error":
                        f"O worker encerrou com código {p.returncode}; operação não considerada confirmada.",
                        "details": data}
            return data
        return {"ok": False, "error": p.stderr.strip() or
                f"Worker terminou sem resultado (código {p.returncode})."}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error":
                "A comunicação com o driver excedeu 60 segundos; o valor não foi confirmado."}
    except (OSError, ValueError, json.JSONDecodeError) as e:
        return {"ok": False, "error": f"Falha ao consultar o worker: {e}"}
    finally:
        try: result_path.unlink()
        except OSError: pass

class UI:
    def __init__(self, root, startup_mode=False):
        self.root = root
        self.startup_mode = startup_mode
        root.title("AMD Clock Boost Fix")
        try:
            root.iconbitmap(default=str(app_icon_path()))
        except (OSError, tk.TclError):
            pass
        root.geometry("700x500")
        root.minsize(620, 450)
        root.resizable(True, True)
        self.status = tk.StringVar(value="Aguardando o driver AMD…" if startup_mode else "Consultando GPUs AMD e o driver…")
        self.summary = tk.StringVar(value="Aguardando identificação…")
        self.current = tk.StringVar(value="")
        self.range_info = tk.StringVar(value="")
        self.detected_profile = None
        self.busy = False
        self.settings = read_settings()
        try:
            if startup_link_path().exists():
                self.settings["startup_enabled"] = True
        except OSError:
            pass
        self.autostart_var = tk.BooleanVar(value=bool(self.settings.get("startup_enabled")))
        frame = ttk.Frame(root, padding=20); frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="AMD Clock Boost Fix", font=("Segoe UI", 15, "bold")).pack(anchor="w")
        ttk.Label(frame, text="GPU identificada", font=("Segoe UI", 10)).pack(anchor="w", pady=(16, 2))
        ttk.Label(frame, textvariable=self.summary, wraplength=620,
                  font=("Segoe UI", 17, "bold")).pack(anchor="w", pady=(0, 8))
        ttk.Label(frame, textvariable=self.current, wraplength=620, justify="left").pack(anchor="w", pady=(0, 4))
        ttk.Label(frame, textvariable=self.range_info, wraplength=620, justify="left").pack(anchor="w", pady=(0, 12))
        self.apply_button = ttk.Button(frame, text="Aplicar referência da GPU",
                                       command=lambda: self.run("apply"), state="disabled")
        self.apply_button.pack(anchor="w", pady=(0, 6))
        self.restore_button = ttk.Button(frame, text="Restaurar clock boost original",
                                         command=lambda: self.run("restore"), state="disabled")
        self.restore_button.pack(anchor="w", pady=(0, 8))
        self.startup_check = ttk.Checkbutton(
            frame, text="Reaplicar automaticamente ao entrar no Windows",
            variable=self.autostart_var, command=self.toggle_autostart, state="disabled")
        self.startup_check.pack(anchor="w", pady=(0, 4))
        self.progress = ttk.Progressbar(frame, mode="indeterminate")
        self.progress.pack(fill="x", pady=(12, 6))
        ttk.Label(frame, textvariable=self.status, wraplength=620, justify="left").pack(fill="x", anchor="w")
        ttk.Label(frame, text="O aplicativo reaplica o limite após o login. O clock instantâneo varia com carga e temperatura.",
                  wraplength=620, justify="left").pack(fill="x", anchor="w", pady=(8, 0))
        if startup_mode:
            self.root.after(15000, self.startup_if_enabled)
        else:
            self.root.after(150, lambda: self.run("check"))
        self.update_control_states()

    def startup_if_enabled(self):
        if self.autostart_var.get():
            self.run("startup")

    def update_control_states(self):
        button_state = "normal" if not self.busy and self.detected_profile else "disabled"
        self.apply_button.configure(state=button_state)
        self.restore_button.configure(state=button_state)
        can_toggle = bool(self.settings.get("profile_name")) and not self.busy
        self.startup_check.configure(state="normal" if can_toggle else "disabled")

    def toggle_autostart(self):
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
                create_startup_shortcut()
                self.status.set("Reaplicação automática ativada para o próximo login.")
            else:
                remove_startup_shortcut()
                write_settings(updated)
                self.status.set("Reaplicação automática desativada.")
            self.settings = updated
        except Exception as exc:
            self.autostart_var.set(previous)
            rollback = dict(self.settings)
            rollback["startup_enabled"] = previous
            try: write_settings(rollback)
            except OSError: pass
            try:
                if previous: create_startup_shortcut()
                else: remove_startup_shortcut()
            except OSError: pass
            messagebox.showerror("Inicialização não alterada", f"Não foi possível atualizar a inicialização do Windows:\n{exc}")
        self.update_control_states()

    def run(self, mode):
        if self.busy: return
        profile_id = self.detected_profile if mode in ("apply", "restore") else None
        if mode in ("apply", "restore") and profile_id not in GPU_PROFILES:
            messagebox.showerror("GPU indisponível", "Não há uma única GPU compatível identificada para esta ação.")
            return
        if mode == "restore" and not messagebox.askyesno(
                "Restaurar clock original",
                "O programa vai restaurar o clock boost padrão reportado pelo driver AMD e desativar a reaplicação automática no login. Deseja continuar?"):
            return
        self.busy = True
        self.update_control_states()
        if mode == "check":
            self.status.set("Consultando as GPUs AMD…")
        elif mode == "startup":
            self.status.set("Aguardando o driver AMD e validando o perfil salvo…")
        elif mode == "restore":
            self.status.set(f"Validando a GPU e restaurando o clock padrão do driver para {profile_id}…")
        else:
            self.status.set(f"Validando novamente a GPU e aplicando a referência de {profile_id}…")
        self.progress.start(12)
        threading.Thread(target=self.work, args=(mode, profile_id), daemon=True).start()

    def work(self, mode, profile_id=None):
        if mode == "startup":
            result = apply_saved_startup_profile()
        else:
            result = run_worker(mode, profile_id)
        try: self.root.after(0, self.done, mode, profile_id, result)
        except tk.TclError: pass

    def done(self, mode, profile_id, result):
        self.progress.stop(); self.busy = False
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
            eligible_adapters = {}
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
                    f"Limite atual: {adapter['current_mhz']} MHz  |  Original da GPU: {adapter['default_mhz']} MHz  |  Referência: {reference} MHz")
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
        if mode == "startup":
            self.status.set(f"Aplicação automática confirmada pelo driver: {applied} MHz.")
            self.update_control_states()
            return

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
                remove_startup_shortcut()
            except OSError as exc:
                warnings.append(f"atalho de inicialização: {exc}")
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
                    f"O driver confirmou o valor original de {applied} MHz, mas não foi possível concluir a desativação da reaplicação automática:\n{detail}")
            else:
                self.status.set(f"Clock boost original restaurado e confirmado pelo driver: {applied} MHz.")
                messagebox.showinfo(
                    "Clock original restaurado",
                    f"{profile}: o clock boost original de {applied} MHz foi restaurado e confirmado pelo driver. A reaplicação automática foi desativada.")
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
                create_startup_shortcut()
        except OSError as exc:
            self.status.set(f"Clock aplicado, mas não foi possível salvar/atualizar a inicialização: {exc}")
        self.update_control_states()
        messagebox.showinfo(
            "Aplicação confirmada",
            f"{result['profile_name']}: referência de {applied} MHz aplicada à GPU detectada e confirmada pelo driver."
        )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", choices=("check", "apply", "restore"))
    parser.add_argument("--profile", choices=tuple(GPU_PROFILES))
    parser.add_argument("--result-file")
    parser.add_argument("--startup-apply", action="store_true")
    parser.add_argument("--silent", action="store_true")
    args = parser.parse_args()
    if args.worker: return worker(args.worker, args.profile, args.result_file)
    cleanup_legacy_restart_confirmation()
    if args.startup_apply:
        time.sleep(15)
        result = apply_saved_startup_profile()
        try:
            write_startup_log(result)
        except OSError:
            pass
        return 0 if result.get("ok") else 1
    root = tk.Tk(); UI(root); root.mainloop(); return 0

if __name__ == "__main__": raise SystemExit(main())

