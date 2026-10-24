# AMD Clock Boost Fix

Aplica referências fixas de clock boost para GPUs AMD Radeon RX 6000 e RX 7000, com identificação automática do modelo.

## Uso

1. Extraia a pasta inteira para um local permanente.
2. Abra **AMDClockBoostFix.exe** e aplique a referência da GPU identificada.
3. Marque **Reaplicar automaticamente ao entrar no Windows** para habilitar a reaplicação após o login.
4. Use **Restaurar clock boost original** para voltar ao valor padrão informado pelo driver AMD. Essa ação desativa a reaplicação automática para que a referência do programa não seja aplicada novamente no próximo login.

A opção cria um atalho na pasta Inicializar do usuário atual. Nas próximas inicializações, o programa espera 15 segundos pelo driver, consulta a GPU e reaplica a referência sem abrir janela. Se a consulta ao driver falhar, faz até cinco tentativas. Se o perfil salvo não corresponder à GPU ou não houver exatamente um perfil compatível, não altera o clock.

Para desativar, desmarque a opção dentro do programa. Também é possível remover o atalho em `shell:startup` ou desativar o app em **Configurações > Aplicativos > Inicialização**. Não é criada tarefa agendada e não é necessário executar como administrador.

## Diagnóstico do modo silencioso

Cada tentativa automática grava o resultado em `%LOCALAPPDATA%\AMDClockBoostFix\startup.log`. O modelo e o clock salvos ficam em `settings.json` na mesma pasta. A janela do programa aparece somente quando ele é aberto manualmente.

A reaplicação acontece após entrar na conta do Windows, não antes da tela de login. O clock é configurado pelo ADLX e confirmado com leitura do driver; não é gravado no firmware/BIOS nem em arquivos do Adrenalin. Se o driver redefinir o valor, a inicialização reaplica a referência salva.

## Perfis incluídos

| Linha | GPU | Clock do perfil |
| --- | --- | ---: |
| RX 6000 | RX 6400 | 2321 MHz |
| RX 6000 | RX 6500 XT | 2815 MHz |
| RX 6000 | RX 6600 | 2491 MHz |
| RX 6000 | RX 6600 XT | 2589 MHz |
| RX 6000 | RX 6650 XT | 2635 MHz |
| RX 6000 | RX 6700 | 2450 MHz |
| RX 6000 | RX 6700 XT | 2581 MHz |
| RX 6000 | RX 6750 XT | 2600 MHz |
| RX 6000 | RX 6800 | 2105 MHz |
| RX 6000 | RX 6800 XT | 2250 MHz |
| RX 6000 | RX 6900 XT | 2250 MHz |
| RX 6000 | RX 6950 XT | 2310 MHz |
| RX 7000 | RX 7400 | 1100 MHz* |
| RX 7000 | RX 7600 | 2655 MHz |
| RX 7000 | RX 7650 GRE | 2695 MHz |
| RX 7000 | RX 7600 XT | 2755 MHz |
| RX 7000 | RX 7700 | 2459 MHz |
| RX 7000 | RX 7700 XT | 2544 MHz |
| RX 7000 | RX 7800 XT | 2430 MHz |
| RX 7000 | RX 7900 GRE | 2245 MHz |
| RX 7000 | RX 7900 XT | 2400 MHz |
| RX 7000 | RX 7900 XTX | 2500 MHz |

Quando a planilha tem dois clocks, foi usado o maior. *A RX 7400 aparece com somente um valor, 1100 MHz, que foi mantido como recebido. A linha “Máquina a Vapor GPU” foi excluída por não ser um modelo Radeon RX.

## Licença e dependências

O código-fonte próprio está sob MIT. A MIT do projeto não cobre as bindings ADLX da AMD incluídas no executável; consulte **THIRD_PARTY_NOTICES.md** antes de redistribuir o binário.
