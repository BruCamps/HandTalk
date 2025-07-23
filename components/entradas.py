import flet as ft
from components.icons import *
from utils.funcoes import *
from core.customTextFields import *
from core.customContainers import *
from core.user_manager import UserManager
from components.mensagens import *

ft.Theme(font_family="InstrumentSans")

# Entradas do Cadastro
nome = CustomTextField(suffix_icon=icon_name, hint_text="Digite seu nome")
email = CustomTextField(suffix_icon=icon_mail, hint_text="Digite seu email")
senha = PasswordTextField(icon_regular_closed=icon_eyeoff_senha, hint_text="Digite sua senha")

confirmacao_senha = PasswordTextField(icon_regular_closed=icon_eyeoff_confirma_senha, hint_text="Confirme sua senha")

# Entradas do Login
email_login = CustomTextField(suffix_icon=icon_mail_login, hint_text="Digite seu email")
senha_login = PasswordTextField(icon_regular_closed=icon_eyeoff_senha_login, hint_text="Digite sua senha")

# Entradas do Editar Perfil
nome_perfil = CustomTextField(suffix_icon=icon_name_perfil, hint_text="Digite seu nome")
email_perfil = CustomTextField(suffix_icon=icon_mail_perfil, hint_text="Digite seu email")
senha_perfil = PasswordTextField(icon_regular_closed=icon_eyeoff_senha_perfil, hint_text="Digite sua senha atual")
senha_nova_perfil = PasswordTextField(icon_regular_closed=icon_eyeoff_nova_senha_perfil, hint_text="Digite sua nova senha")

# Entradas do Recuperar Senha
email_recuperacao = CustomTextField(suffix_icon=icon_mail_recuperacao, hint_text="Digite seu email")
senha_nova_recuperacao = PasswordTextField(icon_regular_closed=icon_eyeoff_senha_recuperacao, hint_text="Digite sua nova senha")
confirmacao_senha_recuperacao = PasswordTextField(icon_regular_closed=icon_eyeoff_confirma_senha_recuperacao, hint_text="Confirme sua senha")

"""
        Containers de Entradas
"""

# Containers do Cadastro
container_nome = InputContainer(nome, margin=0)
container_email = InputContainer(email, margin=0)
container_senha = InputContainer(senha, margin=0)
container_confirmacao_senha = InputContainer(confirmacao_senha, margin=0)

# Containers do Login
container_email_login = InputContainer(email_login, margin=0)
container_senha_login = InputContainer(senha_login, margin=0)

# Containers do Editar Perfil
container_nome_perfil = InputContainer(nome_perfil)
container_email_perfil = InputContainer(email_perfil)
container_senha_perfil = InputContainer(senha_perfil)
container_senha_nova_perfil = InputContainer(senha_nova_perfil)

# Containers do Recuperar Senha
container_recuperacao_email = InputContainer(email_recuperacao)
container_senha_recuperacao = InputContainer(senha_nova_recuperacao)
container_confirmacao_senha_recuperacao = InputContainer(confirmacao_senha_recuperacao)
