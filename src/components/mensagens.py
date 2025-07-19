import flet as ft

ft.Theme(font_family="InstrumentSans")

# Mensagens de Erro - Cadastro
nome_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
email_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
senha_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
confirmacao_senha_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
geral_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)

# Mensagens de Erro - Login
l_email_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
l_senha_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
mensagem = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)

# Mensagens de Erro - Perfil
nome_perfil_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
email_perfil_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
senha_perfil_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
nova_senha_perfil_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
geral_perfil_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)

# Mensagens de Erro - Recuperação
rec_email_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
rec_senha_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)
rec_confirmacao_senha_msg = ft.Text(color="red", font_family="InstrumentSans SemiBold", size=14, width=343, visible=False)