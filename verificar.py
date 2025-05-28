# from email.mime.text import MIMEText
# import random
# import smtplib
import re


# Regular Expression para o padrão de email
padrao_email = r'[a-zA-Z0-9.]+@ufrpe\.br'

# Verificação do campo Nome
def Nome():
    # Repetição para verificar o nome até que atenda ao padrão
    while True:
        
        # Variável que recebe o nome
        nome = input("Informe o nome: ").strip().title()

        # Verifica se o campo foi preenchido
        if not nome:
            print("\033[31mCampo obrigatório!\033[0;0m")
            continue
        elif any(i.isdigit() for i in nome):
            print("\033[31mNão é válido utilização de números.\033[0;0m")
            continue
        elif(re.search(r'[^a-zA-Z0-9]', nome)):
            print("Possui caracteres. Não é aceito.")    
            continue
        # Verifica se o nome contém algo que não seja letra
        elif (re.search(r'[a-zA-Z]', nome)):
            # Retorna o nome caso ele seja válido
            return nome

        print("\033[31mInsira um nome válido.\033[0;0m")

# Verificação do campo Senha
def Senha():
    # Repetição para verificar a senha até que atenda ao padrão
    while True:
        # Instruções de senha
        print("\033[32mSua senha deve conter pelo menos 6 caracteres, uma letra maiúscula e um caractere especial.\033[0;0m")
        # Variável que recebe a senha
        senha = input("Informe sua senha: ").strip()
        
        # Verifica se o campo foi preenchido
        if not senha:
            print("\033[31mCampo obrigatório!\033[0;0m")
            continue
        # Verifica se a senha contém espaços
        if " " in senha:
            print("\033[31mA senha não pode conter espaços!\033[0;00m]")
            continue
        # Verifica se a senha tem menos de 6 caracteres
        if len(senha) < 6:
            print("\033[31mA senha deve ter no mínimo 6 caracteres!\033[0;0m")
            continue
        # Verifica se a senha contém uma letra continuea
        if not re.search(r'[A-Z]', senha):
            print("\033[31mA senha deve conter pelo menos uma letra maiúscula!\033[0;0m")
            continue
        # Verifica se a senha contém um caractere especial
        if not re.search(r'[^a-zA-Z0-9]', senha):
            print("\033[31mA senha deve conter pelo menos um caractere especial!\033[0;00m")
            continue

        # Retorna a senha caso ela seja válida 
        return senha

# Verificação do campo Nova Senha
def NovaSenha(senha_atual):
    # Repetição para verificar a nova senha até que atenda ao padrão
    while True:
        # Instruções de senha
        print("\033[32mSua senha deve conter pelo menos 6 caracteres, uma letra maiúscula e um caractere especial.\033[0;0m")
        # Variável que recebe a nova senha
        senha_input = input(f"Nova senha (atual: {senha_atual}): ").strip()

        # Verifica se o campo foi preenchido e retorna a senha atual
        if not senha_input:
            return senha_atual
        # Verifica se a senha contém espaços
        if " " in senha_input:
            print("\033[31mA senha não pode conter espaços!\033[0;0m")
            continue
        # Verifica se a senha tem menos de 6 caracteres
        if len(senha_input) < 6:
            print("\033[31mA senha deve ter no mínimo 6 caracteres!\033[0;0m")
            continue
        # Verifica se a senha contém uma letra maiúscula
        if not re.search(r'[A-Z]', senha_input):
            print("\033[31mA senha deve conter pelo menos uma letra maiúscula!\033[0;0m")
            continue
        # Verifica se a senha não contém um caractere especial
        if not re.search(r'[a-zA-Z0-9]', senha_input):
            print("\033[31mA senha deve conter pelo menos um caractere especial!\033[0;0m")
            continue

        # Retorna a nova senha caso ela seja válida
        return senha_input

# Verificação do campo Confirma Senha
def ConfirmaSenha(senha):
    # Repetição para verificar a senha até que atenda ao padrão
    while True:
        # Variável que recebe a senha
        confirmaSenha = input("Confirme a senha: ").strip()

        # Verifica se o campo foi preenchido
        if not confirmaSenha:
            print("\033[31mCampo obrigatório!\033[0;0m")
            continue
        # Verifica se as senhas são iguais
        elif confirmaSenha != senha:
            print("\033[31mAs senhas são diferentes!\033[0;00m")
            continue

        # Retorna a senha caso ela seja válida
        return confirmaSenha

# Verificação do campo Email
def Email():
    # Repetição para verificar o email até que atenda ao padrão
    while True:
        # Variável que recebe o email
        email = input("Informe o email: ").strip().lower()

        # Verifica se o campo foi preenchido
        if not email:
            print("\033[31mCampo obrigatório!\033[0;0m")
            continue
        # Verifica se o email possui espaços
        if " " in email:
            print("\033[31mO email não pode conter espaços!\033[0;0m")
            continue
        elif not (re.search(r'[^.]', email)):
            print("\033[31mO email não pode conter outros caracteres especiais exceto .\033[0;0m")
            continue
        # Verifica se o email está em um formato válido e retorna seu valor
        elif (re.match(padrao_email, email)):
            return email

        # Mensagem para informar que o email é inválido
        print("\033[31mEmail inválido. O email deve ser válido e do domínio '@ufrpe.br'.\033[0;0m")
        continue

# def validar_email(email):
#     regex = r"^[a-zA-Z0-9.]+@[a-zA-Z0-9-] +\.[A-Za-z0-9-.]+$"
#     return re.match(regex, email) is not None

# def enviar_codigo(email):
#     codigo = str(random.randint(100000 , 999999))

#     remetente = "handtalk.bsi@gmail.com"
#     senha_app = "uocuaacfceziatkz"
#     assunto = "Código de autenticação HandTalk"
#     mensagem = f"seu código de autenticação é: {codigo}"

#     msg = MIMEText(mensagem, "plain", "utf-8")
#     msg["Suject"] = assunto
#     msg["From"] = remetente
#     msg["To"] = email

#     try:
#         with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
#             servidor.starttls()
#             servidor.login(remetente, senha_app)
#             servidor.sendmail(remetente, email, msg.as_string())
#         print("Código enviado para o seu email!")
#         return codigo
#     except Exception as e:
#         print("Erro ao enviar email: ", e)
#         return None
    

# Verificação do campo Novo Email
def NovoEmail(email_atual):
    # Repetição para verificar o email até que atenda ao padrão
    while True:
        # Variável que recebe o email
        email = input(f"Novo email (atual: {email_atual}): ").strip().lower()

        # Verifica se o campo foi preenchido e retorna o email atual
        if not email or email == email_atual:
            return email_atual
        # Verifica se o email está em um formato válido e retorna seu valor
        elif (re.match(padrao_email, email)):
            return email

        # Mensagem para informar que o email é inválido
        print("\033[31mEmail inválido. O email deve ser válido e do domínio '@ufrpe.br'.\033[0;0m")
        continue

# Verificação do campo Usuário
def Usuario():
    # Repetição para verificar o usuário até que atenda ao padrão
    while True:
        # Variável que recebe o nome de usuário
        usuario = input("Informe o nome de usuário: ").strip()

        # Verifica se o campo foi preenchido
        if not usuario:
            print("\033[31mCampo obrigatório!\033[0;0m")
            continue
        # Verifica se o nome de usuário contém espaços
        if " " in usuario:
            print("\033[31mO nome de usuário não pode conter espaços!\033[0;0m")
            continue
        # Verifica se o nome de usuário contém apenas letras, números e os seguintes caracteres: . _ -
        if (re.search(r'[^a-zA-Z0-9._-]', usuario)):
            print("\033[31mO nome de usuário pode conter apenas letras, números e os seguintes caracteres: . _ -!\033[0;0m")
            continue
        
        # Retorna o nome de usuário caso ele seja válido
        return usuario

# Verificação do campo Novo Usuário
def NovoUsuario(usuario_atual):
    # Repetição para verificar o nome de usuário até que atenda ao padrão
    while True:
        # Variável que recebe o novo nome de usuário
        usuario_input = input(f"Novo nome de usuário (atual: {usuario_atual}): ").strip()
        
        # Verifica se o campo foi preenchido e retorna o nome de usuário atual
        if not usuario_input or usuario_input == usuario_atual:
            return usuario_atual
        # Verifica se o nome de usuário contém espaços
        if " " in usuario_input:
            print("\033[31mO nome de usuário não pode conter espaços!\033[0;0m")
            continue
        # Verifica se o nome de usuário contém apenas letras, números e os caracteres: . _ -
        if (re.match(r'[^a-zA-Z0-9._-]', usuario_input)):
            print("\033[31mO nome de usuário pode conter apenas letras, números e os seguintes caracteres: . _ -!\033[0;0m")
            continue
        
        # Retorna o nome de usuário caso ele seja válido
        return usuario_input