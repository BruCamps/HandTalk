import defs

def Nome():
    while True:
        # Entrada do nome e remoção de espacos
        nome = input("Informe o nome: ").strip()
        # Verifica se o campo está vazio
        if not nome:
            print("\033[31mCampo obrigatório!\033[0;0m")

        for i in nome:
            # Verifica se o nome contém números ou caracteres especiais
            if i.isdigit() or i in '!@#$% ̈&*()_+-=,./?`~':
                print("\033[31mDigite um nome válido.\033[0;0m")
                break
        else:
            return nome.strip()

def Senha():
    while True:
        # Entrada da senha e remoção de espacos
        senha = input("Informe a senha: ").strip()
        # Verifica se o campo está vazio
        if not senha:
            print("\033[31mCampo obrigatório!\033[0;0m")
        # Verifica se a senha tem menos de 6 caracteres
        elif len(senha) < 6:
            print("\033[31mA senha deve ter no mínimo 6 caracteres!\033[0;0m")
        # Verifica se a senha tem pelo menos uma letra maiúscula
        elif not any(i.isupper() for i in senha):
            print("\033[31mA senha deve conter pelo menos uma letra maiúscula!\033[0;0m")
        # Verifica se a senha tem pelo menos um caractere especial
        elif not any(i in '!@#$% ̈&*()_+-=,./?`~' for i in senha):
            print("\033[31mDeve conter um caractere especial!\033[0;0m")
        else:
            return senha.strip()


def ConfirmaSenha(senha):
    while True:
        # Entrada da senha e remoção de espacos
        confirmaSenha = input("Confirme a senha: ").strip()
        # Verifica se o campo está vazio
        if not confirmaSenha:
            print("\033[31mCampo obrigatório!\033[0;0m")
        # Verifica se as senhas são iguais
        elif confirmaSenha != senha:
            print("\033[31mAs senhas são diferentes!\033[0;0m", senha, confirmaSenha)
        else:
            return confirmaSenha.strip()

def Email():
    while True:
        # Entrada do email e remoção de espacos
        email = input("Informe o email: ").strip()
        # Verifica se o campo está vazio
        if not email:
            print("\033[31mCampo obrigatório!\033[0;0m")
        # Verifica se o email é do domínio @ufrpe.br
        elif '@ufrpe.br' in email:
            return email.strip()
        else:
            print("\033[31mEmail inválido.Deve conter '@ufrpe.br'.\033[0;0m")

def Usuario():
    while True:
        # Entrada do nome de usuário e remoção de espacos
        usuario = input("Informe o nome de usuário: ").strip()
        # Verifica se o campo está vazio
        if not usuario:
            print("\033[31mCampo obrigatório!\033[0;0m")
        else:
            return usuario.strip()