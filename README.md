# AMD Clock Boost Fix

Este app serve para aplicar o clock boost de referência da AMD
Algumas fabricantes elevam o clock boost além do permitido para a GPU, com isso pode ocorrer o erro de tempo limite de driver (AMD Timeout)

## Uso

1. Baixe o **AMDClockBoostFix.exe** e coloque em uma pasta definitiva (Que não será excluida).
2. Abra **AMDClockBoostFix.exe** e aplique a referência da GPU identificada.
3. Marque **Reaplicar automaticamente ao entrar no Windows** para habilitar a reaplicação após o login.
4. Use **Restaurar clock boost original** para voltar ao valor padrão informado pelo driver AMD. Essa ação desativa a reaplicação automática para que a referência do programa não seja aplicada novamente no próximo login.

A opção cria um atalho na pasta Inicializar do usuário atual. Nas próximas inicializações, o programa espera 15 segundos pelo driver, consulta a GPU e reaplica a referência sem abrir janela. Se a consulta ao driver falhar, faz até cinco tentativas. Se o perfil salvo não corresponder à GPU ou não houver exatamente um perfil compatível, não altera o clock.

Para desativar, desmarque a opção dentro do programa. Também é possível remover o atalho em `shell:startup` ou desativar o app em **Configurações > Aplicativos > Inicialização**. Não é criada tarefa agendada e não é necessário executar como administrador.

## Diagnóstico do modo silencioso

Cada tentativa automática grava o resultado em `%LOCALAPPDATA%\AMDClockBoostFix\startup.log`. O modelo e o clock salvos ficam em `settings.json` na mesma pasta. A janela do programa aparece somente quando ele é aberto manualmente.

A reaplicação acontece após entrar na conta do Windows, não antes da tela de login. O clock é configurado pelo ADLX e confirmado com leitura do driver; não é gravado no firmware/BIOS nem em arquivos do Adrenalin. Se o driver redefinir o valor, a inicialização reaplica a referência salva.

## Perfis incluídos

| RX 6000 | 
- RX 6400
- RX 6500 XT
- RX 6600
- RX 6600 XT
- RX 6650 XT
- RX 6700
- RX 6700 XT
- RX 6750 XT
- RX 6800
- RX 6800 XT
- RX 6900 XT
- RX 6950 XT

| RX 7000 | 
RX 7400
RX 7600 
RX 7650 GRE
RX 7600 XT
RX 7700
RX 7700 XT
RX 7800 XT
RX 7900 GRE
RX 7900 XT
RX 7900 XTX


<img width="82" height="261" alt="image" src="https://github.com/user-attachments/assets/807c480b-fd7b-4e7e-9c8d-384273aadadc" />

<img width="81" height="261" alt="image" src="https://github.com/user-attachments/assets/0f4b388b-570e-4aaf-acbe-f84c78280f41" />

## Licença e dependências

O código-fonte próprio está sob MIT. A MIT do projeto não cobre as bindings ADLX da AMD incluídas no executável; consulte **THIRD_PARTY_NOTICES.md** antes de redistribuir o binário.
