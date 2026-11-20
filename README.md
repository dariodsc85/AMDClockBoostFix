# AMD Clock Boost Fix

Utilitário leve para Windows que aplica e mantém o **clock boost de referência oficial** em placas de vídeo AMD Radeon (séries RX 500, RX 6000 e RX 7000) utilizando a API oficial **AMD ADLX**, prevenindo picos de boost acima da especificação de fábrica e instabilidades/timeouts de driver.

---

## Principais Recursos

- **Sem Overclock:** Aplica exclusivamente o clock boost de referência oficial catalogado para o modelo detectado — nunca valores arbitrários.
- **Isolamento de Processo:** Toda a comunicação com a DLL nativa do driver (`ADLX`) ocorre em um processo *worker* isolado, evitando travamentos ou vazamentos de memória na interface.
- **Validação Rigorosa antes de Aplicar:**
  - Verifica o `VendorId` (`1002`) e bloqueia a operação caso mais de uma GPU idêntica seja detectada.
  - Valida se o clock de referência está estritamente dentro dos limites mínimo e máximo reportados pelo driver atual.
  - Realiza leitura de retorno (*readback*) após a escrita para confirmar que o driver aplicou o valor exato.
- **Restauração com 1 Clique:** Restaura o clock boost padrão original reportado pelo driver e desativa a reaplicação automática.
- **Reaplicação Automática no Logon:** Integração nativa via Registro do Windows (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`) com retentativas inteligentes após o login para aguardar a inicialização do driver AMD.

---

## Novidades da Versão 2.4

- **Inicialização via Registro do Windows:** Substituição do atalho na pasta *Inicializar* pela chave `Run` do usuário atual (`HKCU`), migrando e removendo automaticamente atalhos `.lnk` de versões anteriores.
- **Proteção contra Instâncias Simultâneas:** Uso de *Mutex* global no Windows para impedir conflitos entre a interface gráfica e a tarefa automática pós-login.
- **Inicialização mais Rápida:** Atraso inicial pós-login reduzido para 4 segundos com até 8 tentativas automáticas de consulta ao driver.
- **Endurecimento de Segurança e Estabilidade:** Validação estrita do diretório de saída do *worker* em `%LOCALAPPDATA%\AMDClockBoostFix` e ordenação segura na liberação de interfaces COM/ADLX.

---

## GPUs Suportadas

| Série | Modelos Catalogados |
| :--- | :--- |
| **Radeon RX 500** | RX 550, RX 560, RX 570, RX 580, RX 580 2048SP, RX 590 |
| **Radeon RX 6000** | RX 6400, RX 6500 XT, RX 6600, RX 6600 XT, RX 6650 XT, RX 6700, RX 6700 XT, RX 6750 XT, RX 6800, RX 6800 XT, RX 6900 XT, RX 6950 XT |
| **Radeon RX 7000** | RX 7400, RX 7600, RX 7600 XT, RX 7650 GRE, RX 7700, RX 7700 XT, RX 7800 XT, RX 7900 GRE, RX 7900 XT, RX 7900 XTX |

---

## Como Usar

1. Baixe o executável `AMDClockBoostFix.exe` na aba **Releases** (ou execute via Python).
2. Abra o aplicativo e aguarde a identificação automática da sua GPU AMD.
3. Clique em **Aplicar referência da GPU** e aguarde a confirmação do driver.
4. *(Opcional)* Marque **Reaplicar automaticamente ao entrar no Windows** para que o limite seja reaplicado sempre que você fizer login.
5. Para voltar ao comportamento padrão de fábrica da placa, clique em **Restaurar clock boost original**.

> **Nota:** Configurações locais e logs de inicialização são armazenados em `%LOCALAPPDATA%\AMDClockBoostFix\` (`settings.json` e `startup.log`).

---

## Executando ou Compilando a partir do Código-Fonte

### Requisitos
- Windows 10 ou Windows 11 (64-bit)
- Driver AMD Software: Adrenalin Edition instalado
- Python 3.11+

### Execução Direta
```powershell
python amd_clock_boost_fix.py