import os
import verificar

def limpaTerminal():
    # Limpa o terminal
    return os.system('cls' if os.name == 'nt' else 'clear')

def criaBarra():
    print(f"\033[36m{'-' * 32}\033[0;0m")

def menu():
    print(f"\n{'-' * 7} <<< \033[36mHandTalk\033[0;0m >>> {'-' * 7}")
    print("|" + " " * 2 + "\033[36m1\033[0;0m Cadastro" + " " * 18 + "|")
    print("|" + " " * 2 + "\033[36m2\033[0;0m Login" + " " * 21 + "|")
    print("|" + " " * 2 + "\033[36m0\033[0;0m Sair" + " " * 22 + "|")
    # Cria uma barra de divisão
    criaBarra()
    # Escolha da opção
    opcao = input("\033[36mEscolha uma opção: \033[0;0m")
    return opcao

def cadastro():
    # Limpa o terminal
    limpaTerminal()
    print("\033[36mCadastrar\033[0;0m")
    # Verifica o campo Nome
    nome = verificar.Nome()
    # Verifica o campo Usuário
    usuario = verificar.Usuario()
    # Verifica o campo Email
    email = verificar.Email()
    # Verifica o campo Senha
    senha = verificar.Senha()
    # Verifica se as senhas conferem
    confirmaSenha = verificar.ConfirmaSenha(senha)

    limpaTerminal()
    # Cria uma barra de divisão
    criaBarra()
    print("\033[36mCadastro realizado com sucesso!\033[0;0m")
    # Cria uma barra de divisão
    criaBarra()

def login():
    # Limpa o terminal
    limpaTerminal()
    print("\033[36mLogin\033[0;0m")
    # Fazer a lógica do login