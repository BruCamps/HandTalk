import defs

# Limpa o terminal
defs.limpaTerminal()

# Repetição para executar o menu
while True:
    # Armazena a opção escolhida do menu
    escolha = defs.menu()

    # Executa a opção escolhida de acordo com o número
    if escolha == '1':
        defs.cadastro()
    elif escolha == '2':
        defs.login()
    elif escolha == '3':
        defs.run_quiz()
    elif escolha == '4':  
        defs.alterar_usuario()
    elif escolha == '5': 
        defs.excluir_usuario()
    elif escolha == '0':
        print('\033[36mSaindo...\033[0;0m')
        break
    else:
        defs.limpaTerminal()
        defs.criaBarra()
        print('\033[31mOpção inválida!\033[0;0m')
        defs.criaBarra()