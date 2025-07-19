import flet as ft
from core.user_manager import UserManager
from src.components.entradas import *
from src.components.icons import *
from src.components.mensagens import *
from core.state import estado
from core.menu import MenuNavegacao 
import time

global show_password_cadastro, show_password_login, show_confirm_password, show_password_perfil, show_confirm_password_perfil
show_confirm_password_perfil = False
show_password_perfil = False
show_password_cadastro = False
show_password_login = False
show_confirm_password = False

def campo_obrigatorio(
        page: ft.Page, 
        container: ft.Container, 
        campo: ft.TextField, 
        campo_msg: ft.Text,
        icon: ft.Image, 
        icon_red: ft.Image,
        senha_login: ft.TextField = None
    ):
    if not campo.value:
        campo_msg.value = "Campo obrigatório!"
        campo_msg.visible = True
        campo.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        campo.text_style = {
            "color": "#F44336", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        campo.bgcolor = "#FFEAEA"
        container.bgcolor = "#FFEAEA"
        campo.suffix_icon = icon_red
    else:
        campo_msg.visible = False
        campo_msg.value = ""
        campo.bgcolor = "#E7F9FD"
        container.bgcolor = "#E7F9FD"
        campo.suffix_icon = icon
        campo.hint_style = {
            "color": "#5DA6AB", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        if campo == senha_login:
            campo.text_style = {
                "color": "#006A71", 
                "font_family": "InstrumentSans Medium", 
                "letter_spacing": 5, 
                "size": 20
            }
        else:
            campo.text_style = {
                "color": "#006A71", 
                "font_family": "InstrumentSans Medium", 
                "letter_spacing": 0, 
                "size": 20
            }
    page.update()

def autenticar(page: ft.Page, email: ft.TextField, senha: ft.TextField, menu: MenuNavegacao):
    from telas.trilhas import mostrar_trilhas

    estado.usuario_logado = UserManager.login(email.value, senha.value)
    if estado.usuario_logado is None:
        mensagem.value = ""
    elif estado.usuario_logado:
        mensagem.visible = True
        mensagem.value = "Login efetuado com sucesso!"
        mensagem.color = "#006A71"
        time.sleep(2)
        mostrar_trilhas(page, menu)
    else:
        mensagem.value = "Login falhou. Verifique seus dados."
        mensagem.visible = True
        page.update()

def recuperar_senha(page: ft.Page):
    from telas.recuperar_senha import mostrar_recuperar_senha
    mostrar_recuperar_senha(page)

def validar_nome(page: ft.Page, nome: ft.TextField, container_nome: ft.Container, 
    nome_msg: ft.Text, icon_name: ft.Image, icon_red_name: ft.Image):
    if nome.value == "":
        nome.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "size": 20}
        nome.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        nome.bgcolor = "#FFEAEA"
        container_nome.bgcolor = "#FFEAEA"
        nome.suffix_icon = icon_red_name
        nome_msg.value = "Campo obrigatório"
        nome_msg.visible = True
    elif not UserManager.nome_valido(nome.value):
        nome.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "size": 20}
        nome.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        nome.bgcolor = "#FFEAEA"
        container_nome.bgcolor = "#FFEAEA"
        nome.suffix_icon = icon_red_name
        nome_msg.value = "Nome inválido"
        nome_msg.visible = True
    else:
        nome.hint_style = {
            "color": "#006A71", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        nome.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20}
        nome.bgcolor = "#E7F9FD"
        container_nome.bgcolor = "#E7F9FD"
        nome.suffix_icon = icon_name
        nome_msg.value = ""
        nome_msg.visible = False
    page.update()

def validar_email(page: ft.Page, email: ft.TextField, container_email: ft.Container, email_msg: ft.Text,  icon_mail: ft.Image, icon_red_mail: ft.Image):
    if email.value == "":
        email.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        email.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        email.suffix_icon = icon_red_mail
        email.bgcolor = "#FFEAEA"
        container_email.bgcolor = "#FFEAEA"
        email_msg.value = "Campo obrigatório"
        email_msg.visible = True
    elif not UserManager.email_valido(email.value):
        email.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        email.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        email.suffix_icon = icon_red_mail
        email.bgcolor = "#FFEAEA"
        container_email.bgcolor = "#FFEAEA"
        email_msg.value = "Formato de email inválido"
        email_msg.visible = True
    else:
        email.hint_style = {
            "color": "#006A71", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        email.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        email.suffix_icon = icon_mail
        email.bgcolor = "#E7F9FD"
        container_email.bgcolor = "#E7F9FD"
        email_msg.value = ""
        email_msg.visible = False
    page.update()

def validar_senha(page: ft.Page, senha: ft.TextField, container_senha: ft.Container, senha_msg: ft.Text, 
icon_eyeoff_senha: ft.Image, icon_eyeon_senha: ft.Image, icon_red_eyeoff_senha: ft.Image, icon_red_eyeon_senha: ft.Image):
    if senha.value == "":
        container_senha.bgcolor = "#FFEDED"
        senha.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        senha.suffix_icon = icon_red_eyeoff_senha
        senha.bgcolor = "#FFEDED"
        senha_msg.value = "Campo obrigatório"
        senha_msg.visible = True
    elif not UserManager.senha_valida(senha.value):
        senha.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        container_senha.bgcolor = "#FFEDED"
        senha.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha.suffix_icon = icon_red_eyeoff_senha
        senha.bgcolor = "#FFEDED"
        senha_msg.value = "A senha deve ter no mínimo 6 caracteres"
        senha_msg.visible = True
    else:
        senha.hint_style = {
            "color": "#006A71", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        container_senha.bgcolor = "#E7F9FD"
        senha.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha.suffix_icon = icon_eyeoff_senha
        senha.bgcolor = "#E7F9FD"
        senha_msg.value = ""
        senha_msg.visible = False
    page.update()

def validar_confirmacao_senha(page: ft.Page, senha: ft.TextField, confirmacao_senha: ft.TextField, container_confirmacao_senha: ft.Container, confirmacao_senha_msg: ft.Text):
    if confirmacao_senha.value == "":
        container_confirmacao_senha.bgcolor = "#FFEDED"
        confirmacao_senha.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        confirmacao_senha.bgcolor = "#FFEDED"
        confirmacao_senha.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        confirmacao_senha.suffix_icon = icon_red_eyeoff_confirma_senha
        confirmacao_senha_msg.value = "Campo obrigatório"
        confirmacao_senha_msg.visible = True
    elif senha.value != confirmacao_senha.value:
        confirmacao_senha.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        container_confirmacao_senha.bgcolor = "#FFEDED"
        confirmacao_senha.bgcolor = "#FFEDED"
        confirmacao_senha.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        confirmacao_senha.suffix_icon = icon_red_eyeoff_confirma_senha
        confirmacao_senha_msg.value = "As senhas devem ser iguais"
        confirmacao_senha_msg.visible = True
    else:
        confirmacao_senha.hint_style = {
            "color": "#006A71", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        container_confirmacao_senha.bgcolor = "#E7F9FD"
        confirmacao_senha.bgcolor = "#E7F9FD"
        confirmacao_senha.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        confirmacao_senha.suffix_icon = icon_eyeoff_confirma_senha
        confirmacao_senha_msg.value = ""
        confirmacao_senha_msg.visible = False
    page.update()

def validar_senha_atual(page: ft.Page, senha: ft.TextField, container_senha: ft.Container,senha_msg: ft.Text, 
icon_eyeon_senha: ft.Image, icon_eyeoff_senha: ft.Image, icon_red_eyeon_senha: ft.Image, icon_red_eyeoff_senha: ft.Image):
    if senha.value == "":
        container_senha.bgcolor = "#FFEDED"
        senha.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        senha.suffix_icon = icon_red_eyeoff_senha
        senha.bgcolor = "#FFEDED"
        senha_msg.value = "Campo obrigatório"
        senha_msg.visible = True
    else:
        senha.hint_style = {
            "color": "#006A71", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        container_senha.bgcolor = "#E7F9FD"
        senha.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha.suffix_icon = icon_eyeoff_senha
        senha.bgcolor = "#E7F9FD"
        senha_msg.value = ""
        senha_msg.visible = False
    page.update()

def validar_nova_senha(page: ft.Page, senha: ft.TextField, nova_senha: ft.TextField, container_senha: ft.Container, nova_senha_msg: ft.Text, icon_eyeon_senha: ft.Image, icon_eyeoff_senha: ft.Image, icon_red_eyeon_senha: ft.Image, icon_red_eyeoff_senha: ft.Image):
    if nova_senha.value == "":
        container_senha.bgcolor = "#FFEDED"
        senha.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        senha.suffix_icon = icon_red_eyeoff_senha
        senha.bgcolor = "#FFEDED"
        senha_msg.value = "Campo obrigatório"
        senha_msg.visible = True
    elif not UserManager.nova_senha_valida(senha.value, nova_senha.value):
        senha.hint_style = {
            "color": "#FF9898", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        container_senha.bgcolor = "#FFEDED"
        senha.text_style={"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.suffix_icon = icon_red_eyeoff_senha
        senha.bgcolor = "#FFEDED"
        senha_msg.value = "A senha deve ser diferente da antiga"
        senha_msg.visible = True
    else:
        senha.hint_style = {
            "color": "#006A71", 
            "font_family": "InstrumentSans Medium", 
            "letter_spacing": 0, 
            "size": 20
        }
        container_senha.bgcolor = "#E7F9FD"
        senha.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha.suffix_icon = icon_eyeoff_senha
        senha.bgcolor = "#E7F9FD"
        senha_msg.value = ""
        senha_msg.visible = False
    page.update()

def toggle_password_cadastro(page: ft.Page, senha: ft.TextField, container_senha: ft.Container):
    global show_password_cadastro
    show_password_cadastro = not show_password_cadastro
    if show_password_cadastro and UserManager.senha_valida(senha.value):
        senha.suffix_icon = icon_eyeon_senha
        senha.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.password = False
        container_senha.bgcolor = "#E7F9FD"
        senha.bgcolor = "#E7F9FD"
    elif (senha.value == "" or not UserManager.senha_valida(senha.value)) and not show_password_cadastro:
        senha.suffix_icon = icon_red_eyeon_senha
        senha.hint_style = {"color": "#FF9898", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.text_style = {"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha.password = False
        senha.bgcolor = "#FFEDED"
        container_senha.bgcolor = "#FFEDED"
    elif (senha.value == "" or not UserManager.senha_valida(senha.value)) and show_password_cadastro:
        container_senha.bgcolor = "#FFEDED"
        senha.suffix_icon = icon_red_eyeoff_senha
        senha.bgcolor = "#FFEDED"
        senha.hint_style = {"color": "#FF9898", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.text_style = {"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.password = True
    else:
        container_senha.bgcolor = "#E7F9FD"
        senha.bgcolor = "#E7F9FD"
        senha.suffix_icon = icon_eyeoff_senha
        senha.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha.password = True
    page.update()

def toggle_password_login(page: ft.Page, senha_login: ft.TextField, container_senha_login: ft.Container):
    global show_password_login
    show_password_login = not show_password_login
    if show_password_login:
        senha_login.suffix_icon = icon_eyeon_senha_login
        senha_login.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha_login.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha_login.password = False
        container_senha_login.bgcolor = "#E7F9FD"
        senha_login.bgcolor = "#E7F9FD"
    else:
        container_senha_login.bgcolor = "#E7F9FD"
        senha_login.bgcolor = "#E7F9FD"
        senha_login.suffix_icon = icon_eyeoff_senha_login
        senha_login.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha_login.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha_login.password = True
    page.update()

def toggle_password_perfil(page: ft.Page, senha_perfil: ft.TextField, container_senha_perfil: ft.Container):
    global show_password_perfil
    show_password_perfil = not show_password_perfil
    if show_password_perfil:
        senha_perfil.suffix_icon = icon_eyeon_senha_perfil
        senha_perfil.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha_perfil.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha_perfil.password = False
        container_senha_perfil.bgcolor = "#E7F9FD"
        senha_perfil.bgcolor = "#E7F9FD"
    else:
        container_senha_perfil.bgcolor = "#E7F9FD"
        senha_perfil.bgcolor = "#E7F9FD"
        senha_perfil.suffix_icon = icon_eyeoff_senha_perfil
        senha_perfil.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        senha_perfil.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        senha_perfil.password = True
    page.update()
    
def toggle_confirm_password(page: ft.Page, confirmacao_senha: ft.TextField, senha: ft.TextField, container_confirmacao_senha: ft.Container):

    global show_confirm_password

    show_confirm_password = not show_confirm_password
    if show_confirm_password:
        confirmacao_senha.suffix_icon = icon_eyeon_confirma_senha
        confirmacao_senha.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        confirmacao_senha.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        confirmacao_senha.password = False
        container_confirmacao_senha.bgcolor = "#E7F9FD"
        confirmacao_senha.bgcolor = "#E7F9FD"
    elif confirmacao_senha.value == "" or confirmacao_senha.value != senha.value:
        confirmacao_senha.hint_style = {"color": "#FF9898", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        confirmacao_senha.text_style = {"color": "#F44336", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        confirmacao_senha.suffix_icon = icon_red_eyeoff_confirma_senha
        confirmacao_senha.password = False
        confirmacao_senha.bgcolor = "#FFEDED"
        container_confirmacao_senha.bgcolor = "#FFEDED"
    else:
        container_confirmacao_senha.bgcolor = "#E7F9FD"
        confirmacao_senha.bgcolor = "#E7F9FD"
        confirmacao_senha.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        confirmacao_senha.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        confirmacao_senha.suffix_icon = icon_eyeoff_confirma_senha
        confirmacao_senha.password = True
    page.update()

def toggle_new_password_perfil(page: ft.Page, nova_senha_perfil: ft.TextField, senha_perfil: ft.TextField, container_nova_senha_perfil: ft.Container):
    global show_confirm_password_perfil
    show_confirm_password_perfil = not show_confirm_password_perfil

    if show_confirm_password_perfil:
        nova_senha_perfil.suffix_icon = icon_eyeon_nova_senha_perfil
        nova_senha_perfil.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        nova_senha_perfil.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        nova_senha_perfil.password = False
        container_nova_senha_perfil.bgcolor = "#E7F9FD"
        nova_senha_perfil.bgcolor = "#E7F9FD"
    else:
        container_nova_senha_perfil.bgcolor = "#E7F9FD"
        nova_senha_perfil.bgcolor = "#E7F9FD"
        nova_senha_perfil.suffix_icon = icon_eyeoff_nova_senha_perfil
        nova_senha_perfil.hint_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        nova_senha_perfil.text_style = {"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        nova_senha_perfil.password = True
    page.update()
