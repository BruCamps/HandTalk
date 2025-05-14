import defs

defs.limpaTerminal()

while True:
    escolha = defs.menu()

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