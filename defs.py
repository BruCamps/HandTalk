import os
import verificar

# Função para limpar o terminal
def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

# Função para criar uma barra (visual)
def criaBarra():
    print(f"\033[36m{'-' * 40}\033[0;0m")

# Função para exibir o menu principal
def menu():
    print(f"\n{'-' * 7} <<< \033[36mHandTalk\033[0;0m >>> {'-' * 7}")
    print("|" + " " * 2 + "\033[36m1\033[0;0m Cadastro" + " " * 18 + "|")
    print("|" + " " * 2 + "\033[36m2\033[0;0m Login" + " " * 21 + "|")
    print("|" + " " * 2 + "\033[36m3\033[0;0m Quiz"  + " " * 22 + "|")
    print("|" + " " * 2 + "\033[36m4\033[0;0m Atualizar Dados"  + " " * 11 + "|")
    print("|" + " " * 2 + "\033[36m5\033[0;0m Excluir Dados"  + " " * 13 + "|")
    print("|" + " " * 2 + "\033[36m0\033[0;0m Sair"   + " " * 22 + "|")
    criaBarra()
    opcao = input("\033[36mEscolha uma opção: \033[0;0m")
    return opcao

# Função para cadastrar um novo usuário
def cadastro():
    limpaTerminal()
    print("\033[36mCadastrar\033[0;0m")
    nome = verificar.Nome()
    usuario = verificar.Usuario()
    email = verificar.Email()
    senha = verificar.Senha()
    confirmaSenha = verificar.ConfirmaSenha(senha)
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario},{email},{senha}\n")
    limpaTerminal()
    criaBarra()
    print("\033[36mCadastro realizado com sucesso!\033[0;0m")
    criaBarra()

# Função para efetuar o login
def login():
    limpaTerminal()
    print("\033[36mLogin\033[0;0m")
    usuario_email = verificar.Email()
    usuario_senha = verificar.Senha()

    # Verifica se o email e a senha existem no arquivo
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            usuario, email, senha_cadastrada = linha.strip().split(",")
            if usuario_email in (usuario, email) and usuario_senha == senha_cadastrada:
                print("\033[32mLogin realizado com sucesso!\033[0;0m")
                return usuario_email

    print("\033[31mUsuário ou email não encontrados!\033[0;0m")
    return None

# Função para alterar os dados de um usuário
def alterar_usuario():
    # Recebe o email do usuário que deseja alterar
    email_procura = input("Informe o email do usuário que deseja alterar: ").strip().lower()

    # Verifica se o email existe no arquivo
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    registro_encontrado = False
    registros_atualizados = []

    # Percorre as linhas do arquivo
    for linha in linhas:
        usuario, email, senha = linha.strip().split(",")

        # Verifica se o email do usuário correspondente ao email procurado
        if email.strip().lower() == email_procura:
            registro_encontrado = True
            senha_atual = input("Confirme sua senha atual: ").strip()

            # Verifica se as senhas conferem para permitir a alteração
            if senha_atual != senha:
                print("\033[31mSenha incorreta. Cancelando alteração.\033[0;0m")
                registros_atualizados.append(linha)

            # Chama a função para atualizar os dados
            novo_usuario, novo_email, nova_senha = atualizar_dados(usuario, email, senha)

            # Adiciona as informações atualizadas ao arquivo
            registros_atualizados.append(f"{novo_usuario},{novo_email},{nova_senha}\n")

        # Adiciona as linhas que não foram modificadas ao arquivo 
        registros_atualizados.append(linha)

    # Atualiza o arquivo
    if registro_encontrado:
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(registros_atualizados)
        print("\033[32mInformações atualizadas com sucesso!\033[0;0m")
    # Mensagem para informar que o registro não foi encontrado
    print("\033[31mRegistro não encontrado!\033[0;0m")

# Função para atualizar os dados de um usuário
def atualizar_dados(usuario_atual, email_atual, senha_atual):
    print("Registro encontrado! Insira os novos dados (ou deixe em branco para manter o atual).")

    # Atualiza o nome de usuário:
    usuario_input = verificar.NovoUsuario(usuario_atual)
    novo_usuario = usuario_input

    # Atualiza o email:
    email_input = verificar.NovoEmail(email_atual) 
    novo_email = email_input

    # Atualiza a senha:
    senha_input = verificar.NovaSenha(senha_atual)
    nova_senha = senha_input

    # Retorna os dados atualizados
    return novo_usuario, novo_email, nova_senha

# Função para excluir um usuário
def excluir_usuario():
    # Recebe o email do usuário que deseja excluir
    email_procura = input("Informe o email do usuário que deseja excluir: ").strip().lower()

    # Verifica se o email existe no arquivo
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    registro_encontrado = False
    registros_atualizados = []

    # Percorre as linhas do arquivo
    for linha in linhas:
        usuario, email, senha = linha.strip().split(",")

        # Verifica se o email do usuário correspondente ao email procurado
        if email.strip().lower() == email_procura:
            registro_encontrado = True
            senha_atual = input("Confirme sua senha atual: ").strip()

            # Verifica se as senhas conferem para permitir a exclusão
            if senha_atual != senha:
                print("\033[31mSenha incorreta. Cancelando exclusão.\033[0;0m")
                registros_atualizados.append(linha)
                continue

            # Mensagem para informar que o usuário foi removido
            print(f"Usuário '{usuario}' removido.")

        # Adiciona as linhas que não foram modificadas ao arquivo
        registros_atualizados.append(linha)

    # Atualiza o arquivo
    if registro_encontrado:
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(registros_atualizados)
        print("\033[32mRegistro excluído com sucesso!\033[0;0m")
    # Mensagem para informar que o registro não foi encontrado
    print("\033[31mRegistro não encontrado!\033[0;0m")

# Função para exibir uma caixa de opções (visual)
def print_option_box(index_pergunta, texto_pergunta, width=50):
    content = f"{index_pergunta}. {texto_pergunta}"
    border = "+" + "-" * (width - 2) + "+"
    print(border)
    print("|" + content.ljust(width - 2) + "|")
    print(border)

# Função para executar o quiz
def run_quiz():
    # Link para o vídeo explicativo
    VIDEO_LINK = "https://youtu.be/UHi8K8XjjNY?si=xVeMwD5YhUP3Docl"

    print("\n==========================================")
    print("           QUIZ DE PORTUGOL              ")
    print("==========================================")
    print("\nBem-vindo ao Quiz de Portugol!")
    print("Descubra um universo lógico onde a sintaxe se transforma em poesia.")
    print("Para se inspirar, assista ao vídeo explicativo:")
    print(VIDEO_LINK)
    print("Caso o link não seja clicável, copie e cole-o na barra de endereço do seu navegador.")
    print("Responda as questões e teste seu conhecimento.\n")

    # Dicionário com as perguntas, opções e respostas corretas
    perguntas = [
        {
            "question": "O que são algoritmos??",
            "options": {
                "A": "Um sistema operacional utilizado para gerenciar hardware.",
                "B": "Um conjunto de dados armazenados em um banco de dados.",
                "C": "Um programa de computador que executa tarefas automaticamente.",
                "D": "Uma sequência de passos finitos e ordenados visando a solução de um problema."
            },
            "correct": "D"
        },
        {
            "question": "Quais são as três formas principais de representar algoritmos?",
            "options": {
                "A": "Código binário, fluxograma e descrição narrativa.",
                "B": "Descrição narrativa, fluxograma e pseudocódigo.",
                "C": "Linguagem de máquina, pseudocódigo e fluxograma.",
                "D": "Banco de dados, fluxograma e descrição narrativa."
            },
            "correct": "B"
        },
        {
            "question": "Qual é a ferramenta mais usada para programar em Portugol?",
            "options": {
                "A": "Visual Studio Code",
                "B": "NetBeans",
                "C": "Portugol Studio",
                "D": "Eclipse"
            },
            "correct": "C"
        }
    ]

    # Variáveis de controle
    max_tentativas = 3
    pontos = 0
    index_questao_atual = 0
    sair_quiz = False

    # Loop principal do quiz
    while index_questao_atual < len(perguntas):

        # Variáveis de controle
        pergunta = perguntas[index_questao_atual]
        tentativas = 0
        voltar_questao = False

        # Loop até atingir o limite de 3 tentativas
        while tentativas < max_tentativas:
            print("\n------------------------------------------")
            print(f"Pergunta {index_questao_atual + 1}: {pergunta['question']}\n")

            # Exibe as opções
            for letra, texto_pergunta in pergunta["options"].items():
                print_option_box(letra, texto_pergunta)

            print("\nResponda com A, B, C ou D.")

            # Exibe opções adicionais
            if index_questao_atual > 0:
                print("Digite 'v' para voltar à pergunta anterior.")
            print("Digite 'p' para pular essa pergunta.")
            print("Digite 'q' para sair do quiz e voltar ao menu.")

            # Recebe a opção/resposta do usuário
            resposta = input("Sua resposta: ").strip().upper()

            # Verifica se o usuário quer sair
            if resposta == "Q":
                print("Saindo do quiz e voltando ao menu...")
                sair_quiz = True
                break

            # Verifica se o usuário quer voltar
            if resposta == "V":
                if index_questao_atual > 0:
                    index_questao_atual -= 1
                    voltar_questao = True
                    print("Voltando para a pergunta anterior...")
                    break
                else:
                    print("Você está na primeira pergunta, não é possível voltar.")
                    continue

            # Verifica se o usuário quer pular
            if resposta == "P":
                print("Você optou por pular esta pergunta.")
                break

            # Verifica se a resposta do usuário está dentro das opções da pergunta
            if resposta in ['A', 'B', 'C', 'D']:
                # Verifica se a resposta do usuário é correta
                if resposta == pergunta["correct"]:
                    print("Resposta correta!")
                    pontos += 1
                    break
                # Caso a resposta seja incorreta, incrementa o contador de tentativas
                else:
                    tentativas += 1
                    if tentativas < max_tentativas:
                        print(f"Resposta incorreta! Você errou {tentativas} vez(es). Tente novamente.")
                    else:
                        print("Você atingiu o número máximo de tentativas para esta pergunta.")
            
            # Caso a resposta seja inválida, exibe uma mensagem de erro e continua o loop
            print("Opção inválida. Digite A, B, C ou D, 'v' para voltar, 'p' para pular ou 'q' para sair.")

        # Verifica se a opção de sair foi escolhida
        if sair_quiz:
            break

        # Verifica se a opção de voltar não foi escolhida e avança para a pergunta seguinte
        if not voltar_questao:
            index_questao_atual += 1

    print("\n==========================================")
    # Verifica se o usuário escolheu sair e exibe uma mensagem
    if sair_quiz:
        print("Quiz interrompido pelo usuário.")
    # Exibe uma mensagem de conclusão
    print("Fim do Quiz!")

    # Mensagem para informar o total de acertos e quantidade de perguntas respondidas
    print(f"Total de acertos: {pontos} de {index_questao_atual} pergunta(s) concluída(s).")
    input("Pressione Enter para voltar ao menu...")