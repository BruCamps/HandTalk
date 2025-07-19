import flet as ft
from core.user_manager import UserManager
from src.components.entradas import *
from src.components.utils.funcoes import *
import core.menu as menu

def mostrar_login(page: ft.Page):
    page.theme = ft.Theme(font_family="InstrumentSans")

    from telas.cadastro import mostrar_cadastro
    email_login.on_change = lambda e: campo_obrigatorio(page, container_email_login, email_login, l_email_msg, icon_mail_login, icon_red_mail_login)
    senha_login.on_change = lambda e: campo_obrigatorio(page, container_senha_login, senha_login, l_senha_msg, icon_eyeoff_senha_login, icon_red_eyeoff_senha_login, senha_login)

    icon_eyeoff_senha_login.on_click = lambda e: toggle_password_login(page, senha_login, container_senha_login)
    icon_eyeon_senha_login.on_click = lambda e: toggle_password_login(page, senha_login, container_senha_login)

    headline = ft.Column([
        ft.Container(
            ft.Text("Login", size=32, text_align="left", width=343, font_family="InstrumentSans SemiBold", color="#006A71"),
            padding=ft.padding.only(top=50),
        ),
        ft.Text("Bem-vindo(a) de volta!", text_align="left", font_family="InstrumentSans Medium", width=343, size=20, color=ft.Colors.GREY_600),
   ], alignment="center", horizontal_alignment="center", spacing=5)

    forms = ft.Column(
        [
            ft.Container(content=headline, padding=ft.padding.only(bottom=20)),
            ft.Container(
                ft.Column([
                    ft.Text("Email", text_align="left", size=18, font_family="InstrumentSans Medium", color="#636262", width=343),
                    container_email_login,
                    l_email_msg
                ], alignment="top", horizontal_alignment="center", spacing=10)
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Senha", text_align="left", size=18, font_family="InstrumentSans Medium", color="#636262", width=343),
                    container_senha_login,
                    l_senha_msg
                ], 
                alignment="top", horizontal_alignment="center", spacing=10)
            ),
            ft.ElevatedButton(
                content=ft.Text(
                    "Esqueci a senha", text_align="right", width=343, size=16, font_family="InstrumentSans Medium", color="#009099",
                    style=ft.TextStyle(
                        decoration=ft.TextDecoration.UNDERLINE, decoration_color="#01C6D3", decoration_style=ft.TextDecorationStyle.SOLID,
                        decoration_thickness=2
                    )
                ),
                bgcolor="transparent", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), shadow_color="transparent", 
                surface_tint_color="transparent", overlay_color="transparent", padding=ft.padding.only(top=10, bottom=10)), 
                on_click= lambda e: recuperar_senha(page)
            ),
            ft.ElevatedButton(
                "Entrar",
                width=343, 
                height=50, 
                style=ft.ButtonStyle(
                    bgcolor="#01C6D3", color="white", shape=ft.RoundedRectangleBorder(radius=10), 
                    shadow_color="transparent", overlay_color="#0ED2E0",
                    text_style=ft.TextStyle(font_family="InstrumentSans Medium", size=20, color="white")
                ), 
                on_click=lambda e: autenticar(page, email_login, senha_login, menu)
            ),
            mensagem
        ],
        alignment="top", horizontal_alignment="center", spacing=20, width=100
    )

    return forms