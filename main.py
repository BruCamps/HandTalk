import defs

# Importa a função limpaTerminal do módulo/arquivo defs
defs.limpaTerminal()

while True:
    # Atribui o retorno da função menu() a variável escolha
    escolha = defs.menu()

    # Leva o usuário para o cadastro 
    if escolha == '1':
        defs.cadastro()
    # Leva o usuário para o login
    elif escolha == '2':
        defs.login()
    # Leva o usuário para o QUIZ
    elif escolha == '3':
        defs.run_quiz()
    elif escolha == '4':  
    # Leva o usuário para atualizar informações
        defs.alterar_usuario()
    elif escolha == '5': 
    # Leva o usuário para excluir cadastro
        defs.excluir_usuario()
    # Finaliza o programa
    elif escolha == '0':
        print('\033[36mSaindo...\033[0;0m')
        break
    else:
        # Limpa o terminal
        defs.limpaTerminal()
        # Cria uma barra de divisão
        defs.criaBarra()
        print('\033[31mOpção inválida!\033[0;0m')
        # Cria uma barra de divisão
        defs.criaBarra()