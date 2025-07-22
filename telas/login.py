import flet as ft
from core.user_manager import UserManager
from components.entradas import *
from utils.funcoes import *
from core.customTexts import *
from core.customContainers import *
from core.customButtons import *
import core.menu as menu

def mostrar_login(page: ft.Page):
    page.theme = ft.Theme(font_family="InstrumentSans")

    from telas.cadastro import mostrar_cadastro

    email_login.on_change = lambda e: campo_obrigatorio(page, container_email_login, email_login, l_email_msg, icon_mail_login, icon_red_mail_login)
    senha_login.on_change = lambda e: campo_obrigatorio(page, container_senha_login, senha_login, l_senha_msg, icon_eyeoff_senha_login, icon_red_eyeoff_senha_login, senha_login)

    icon_eyeoff_senha_login.on_click = lambda e: toggle_password_login(page, senha_login, container_senha_login)
    icon_eyeon_senha_login.on_click = lambda e: toggle_password_login(page, senha_login, container_senha_login)

    forms = ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            content=Heading("Login"), 
                            padding=ft.padding.only(top=50)
                        ),
                        SubHeading(text="Bem-vindo(a) de volta!")
                    ], 
                    alignment="center", horizontal_alignment="center", spacing=5
                ), 
                padding=ft.padding.only(bottom=20)
            ),
            ft.Container(
                ft.Column(
                    [
                        InputLabel("Email"),
                        container_email_login,
                        MessageContainer(content=l_email_msg),
                    ], 
                    alignment="top", horizontal_alignment="center", spacing=10
                )
            ),
            ft.Container(
                ft.Column(
                    [ 
                        InputLabel("Senha"), 
                        container_senha_login, 
                        MessageContainer(content=l_senha_msg)
                    ], 
                    alignment="top", horizontal_alignment="center", spacing=10
                )
            ),
            TransparentButton(
                content=UnderlinedText(text="Esqueci a senha"), width=343, 
                on_click=lambda e: recuperar_senha(page)
            ),
            PrimaryButton(
                text="Entrar", 
                on_click=lambda e: autenticar(page, email_login, senha_login, menu)
            ),
            MessageContainer(content=mensagem)
        ],
        alignment="top", horizontal_alignment="center", spacing=20, width=100
    )

    return forms