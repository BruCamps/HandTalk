import defs

def Nome():
    while True:
        nome = input("Informe o nome: ").strip()
        if not nome:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif any(i.isdigit() for i in nome):
            print("\033[31mDigite um nome válido.\033[0;0m")
        elif any(i in '!@#$% ̈&*()_+-=,./?`~' for i in nome):
            print("\033[31mDigite um nome válido.\033[0;0m")
        else:
            return nome.strip()

def Senha():
    while True:
        senha = input("Informe a senha: ").strip()
        if not senha:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif len(senha) < 6:
            print("\033[31mA senha deve ter no mínimo 6 caracteres!\033[0;0m")
        elif not any(i.isupper() for i in senha):
            print("\033[31mA senha deve conter pelo menos uma letra maiúscula!\033[0;0m")
        elif not any(i in '!@#$% ̈&*()_+-=,./?`~' for i in senha):
            print("\033[31mDeve conter um caractere especial!\033[0;0m")
        else:
            return senha.strip()

def ConfirmaSenha(senha):
    while True:
        confirmaSenha = input("Confirme a senha: ").strip()
        if not confirmaSenha:
            print("\033[31mCampo obrigatório!\033[0;0m")
        elif confirmaSenha != senha:
            print("\033[31mAs senhas são diferentes!\033[0;0m")
        else:
            return confirmaSenha.strip()

def Email():
    while True:
        email = input("Informe o email: ").strip().lower()
        if not email:
            print("\033[31mCampo obrigatório!\033[0;0m")
            continue
        if '@ufrpe.br' in email:
            if not email.startswith('@ufrpe.br'):
                return email
            else:
                print("\033[31mEmail inválido. Deve conter algo antes de '@ufrpe.br'.\033[0;0m")
        else:
            print("\033[31mEmail inválido. Deve conter '@ufrpe.br'.\033[0;0m")

def Usuario():
    while True:
        usuario = input("Informe o nome de usuário: ").strip()
        if not usuario:
            print("\033[31mCampo obrigatório!\033[0;0m")
        else:
            return usuario.strip()