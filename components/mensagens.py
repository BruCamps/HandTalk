import flet as ft
from core.customTexts import *

ft.Theme(font_family="InstrumentSans")

"""
    Mensagens/Feedbacks
"""

# Mensagens do Cadastro
nome_msg = Message()
email_msg = Message()
senha_msg = Message()
confirmacao_senha_msg = Message()
geral_msg = Message()

# Mensagens do Login
l_email_msg = Message()
l_senha_msg = Message()
mensagem = Message()

# Mensagens do Perfil
nome_perfil_msg = Message()
email_perfil_msg = Message()
senha_perfil_msg = Message()
nova_senha_perfil_msg = Message()
geral_perfil_msg = Message()

# Mensagens do Recuperar Senha
rec_email_msg = Message()
rec_senha_msg = Message()
rec_confirmacao_senha_msg = Message()