import os
import verificar

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def criaBarra():
    print(f"\033[36m{'-' * 40}\033[0;0m")

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

def login():
    limpaTerminal()
    print("\033[36mLogin\033[0;0m")
    usuario_email = input("Informe seu usuário ou email: ").strip()
    senha = input("Informe sua senha: ").strip()
    encontrado = False
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            usuario, email, senha_cadastrada = linha.strip().split(",")
            if usuario_email == usuario or usuario_email == email:
                encontrado = True
                if senha == senha_cadastrada:
                    print("\033[32mLogin realizado com sucesso!\033[0;0m")
                    return usuario_email
                else:
                    print("\033[31mSenha incorreta!\033[0;0m")
                    return None
    if not encontrado:
        print("\033[31mUsuário ou email não encontrados!\033[0;0m")
    return None
def alterar_usuario():
    email_procura = input("Informe o email do usuário que deseja alterar: ").strip().lower()

    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    registro_encontrado = False
    registros_atualizados = []

    for linha in linhas:
        usuario, email, senha = linha.strip().split(",")

        if email.strip().lower() == email_procura:
            registro_encontrado = True
            senha_atual = input("Confirme sua senha atual: ").strip()

            if senha_atual != senha:
                print("\033[31mSenha incorreta. Cancelando alteração.\033[0;0m")
                registros_atualizados.append(linha)
                continue

            # **Chamando a função para atualizar os dados**
            novo_usuario, novo_email, nova_senha = atualizar_dados(usuario, email, senha)

            registros_atualizados.append(f"{novo_usuario},{novo_email},{nova_senha}\n")
        else:
            registros_atualizados.append(linha)

    if registro_encontrado:
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(registros_atualizados)
        print("\033[32mInformações atualizadas com sucesso!\033[0;0m")
    else:
        print("\033[31mRegistro não encontrado!\033[0;0m")
def alterar_usuario():
    email_procura = input("Informe o email do usuário que deseja alterar: ").strip().lower()

    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    registro_encontrado = False
    registros_atualizados = []

    for linha in linhas:
        usuario, email, senha = linha.strip().split(",")
        if email.strip().lower() == email_procura:
            registro_encontrado = True
            senha_atual = input("Confirme sua senha atual: ").strip()
            if senha_atual != senha:
                print("\033[31mSenha incorreta. Cancelando alteração.\033[0;0m")
                registros_atualizados.append(linha)
                continue

            novo_usuario, novo_email, nova_senha = atualizar_dados(usuario, email, senha)
            registros_atualizados.append(f"{novo_usuario},{novo_email},{nova_senha}\n")
        else:
            registros_atualizados.append(linha)

    if registro_encontrado:
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(registros_atualizados)
        print("\033[32mInformações atualizadas com sucesso!\033[0;0m")
    else:
        print("\033[31mRegistro não encontrado!\033[0;0m")


def atualizar_dados(usuario_atual, email_atual, senha_atual):
    print("Registro encontrado! Insira os novos dados (ou deixe em branco para manter o atual).")

    # Atualiza o nome de usuário:
    novo_usuario = input(f"Novo nome de usuário (atual: {usuario_atual}): ").strip()
    if not novo_usuario:
        novo_usuario = usuario_atual

    # Atualiza o email:
    email_input = input(f"Novo email (atual: {email_atual}): ").strip().lower()
    if email_input:
        while True:
            if '@ufrpe.br' not in email_input:
                print("\033[31mEmail inválido. Deve conter '@ufrpe.br'.\033[0;0m")
            elif email_input.startswith('@ufrpe.br'):
                print("\033[31mEmail inválido. Deve conter algo antes de '@ufrpe.br'.\033[0;0m")
            else:
                novo_email = email_input
                break
            email_input = input("Novo email (tente novamente): ").strip().lower()
    else:
        novo_email = email_atual

    # Atualiza a senha:
    senha_input = input(f"Nova senha (atual: {senha_atual}): ").strip()
    if senha_input:
        while True:
            if len(senha_input) < 6:
                print("\033[31mA senha deve ter no mínimo 6 caracteres!\033[0;0m")
            elif not any(i.isupper() for i in senha_input):
                print("\033[31mA senha deve conter pelo menos uma letra maiúscula!\033[0;0m")
            elif not any(i in '!@#$%¨&*()_+-=,./?`~' for i in senha_input):
                print("\033[31mDeve conter um caractere especial!\033[0;0m")
            else:
                nova_senha = senha_input
                break
            senha_input = input("Nova senha (tente novamente): ").strip()
    else:
        nova_senha = senha_atual

    return novo_usuario, novo_email, nova_senha

def excluir_usuario():
    email_procura = input("Informe o email do usuário que deseja excluir: ").strip().lower()
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    registro_encontrado = False
    registros_atualizados = []

    for linha in linhas:
        usuario, email, senha = linha.strip().split(",")
        if email.strip().lower() == email_procura:
            registro_encontrado = True
            senha_atual = input("Confirme sua senha atual: ").strip()
            if senha_atual != senha:
                print("\033[31mSenha incorreta. Cancelando exclusão.\033[0;0m")
                registros_atualizados.append(linha)
                continue

            print(f"Usuário '{usuario}' removido.")
        else:
            registros_atualizados.append(linha)

    if registro_encontrado:
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(registros_atualizados)
        print("\033[32mRegistro excluído com sucesso!\033[0;0m")
    else:
        print("\033[31mRegistro não encontrado!\033[0;0m")

def print_option_box(letter, text, width=50):
    content = f"{letter}. {text}"
    border = "+" + "-" * (width - 2) + "+"
    print(border)
    print("|" + content.ljust(width - 2) + "|")
    print(border)
def run_quiz():
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

    questions = [
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

    max_attempts = 3
    score = 0
    current_question_index = 0
    quit_quiz = False

    while current_question_index < len(questions):
        question = questions[current_question_index]
        attempts = 0
        went_back = False

        while attempts < max_attempts:
            print("\n------------------------------------------")
            print(f"Pergunta {current_question_index + 1}: {question['question']}\n")

            for letter, option_text in question["options"].items():
                print_option_box(letter, option_text)

            print("\nResponda com A, B, C ou D.")
            if current_question_index > 0:
                print("Digite 'v' para voltar à pergunta anterior.")
            print("Digite 'p' para pular essa pergunta.")
            print("Digite 'q' para sair do quiz e voltar ao menu.")

            response = input("Sua resposta: ").strip().upper()

            if response == "Q":
                print("Saindo do quiz e voltando ao menu...")
                quit_quiz = True
                break

            if response == "V":
                if current_question_index > 0:
                    current_question_index -= 1
                    went_back = True
                    print("Voltando para a pergunta anterior...")
                    break
                else:
                    print("Você está na primeira pergunta, não é possível voltar.")
                    continue

            if response == "P":
                print("Você optou por pular esta pergunta.")
                break

            if response in ['A', 'B', 'C', 'D']:
                if response == question["correct"]:
                    print("Resposta correta!")
                    score += 1
                    break
                else:
                    attempts += 1
                    if attempts < max_attempts:
                        print(f"Resposta incorreta! Você errou {attempts} vez(es). Tente novamente.")
                    else:
                        print("Você atingiu o número máximo de tentativas para esta pergunta.")
            else:
                print("Opção inválida. Digite A, B, C ou D, 'v' para voltar, 'p' para pular ou 'q' para sair.")

        if quit_quiz:
            break

        if not went_back:
            current_question_index += 1

    print("\n==========================================")
    if quit_quiz:
        print("Quiz interrompido pelo usuário.")
    else:
        print("Fim do Quiz!")

    print(f"Total de acertos: {score} de {current_question_index} pergunta(s) concluída(s).")
    input("Pressione Enter para voltar ao menu...")