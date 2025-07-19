import flet as ft
from core.user_manager import UserManager
import time
from src.components.icons import *
from src.components.utils.funcoes import *
from src.components.entradas import *
from src.components.mensagens import *

def mostrar_cadastro(page: ft.Page):
    page.theme = ft.Theme(font_family="InstrumentSans")

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    icon_eyeoff_senha.on_click = lambda e: toggle_password_cadastro(page, senha, container_senha)
    icon_eyeon_senha.on_click = lambda e: toggle_password_cadastro(page, senha, container_senha)
    icon_red_eyeoff_senha.on_click = lambda e: toggle_password_cadastro(page, senha, container_senha)
    icon_red_eyeon_senha.on_click = lambda e: toggle_password_cadastro(page, senha, container_senha)
    icon_eyeoff_confirma_senha.on_click = lambda e: toggle_confirm_password(page, confirmacao_senha, senha, container_confirmacao_senha)
    icon_eyeon_confirma_senha.on_click = lambda e: toggle_confirm_password(page, confirmacao_senha, senha, container_confirmacao_senha)
    icon_red_eyeoff_confirma_senha.on_click = lambda e: toggle_confirm_password(page, confirmacao_senha, senha, container_confirmacao_senha)
    icon_red_eyeon_confirma_senha.on_click = lambda e: toggle_confirm_password(page, confirmacao_senha, senha, container_confirmacao_senha)

    dialog = ft.AlertDialog(
        title=ft.Text("Atenção", font_family="InstrumentSans SemiBold", size=18),
        content=ft.Text("Preencha todos os campos", font_family="InstrumentSans SemiBold", color="red", size=16),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dialog))],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        actions_padding=20,
        title_padding=20,
        bgcolor="#E0F1F5"
    )
    
    from telas.verificacao_codigo import mostrar_codigo_verificacao_email

    nome.on_change = lambda e: validar_nome(page, nome, container_nome, nome_msg)
    email.on_change = lambda e: validar_email(page, email, container_email, email_msg)
    senha.on_change = lambda e: validar_senha(page, senha, container_senha, senha_msg)
    confirmacao_senha.on_change = lambda e: validar_confirmacao_senha(page, senha, confirmacao_senha, container_confirmacao_senha, confirmacao_senha_msg)
    
    def ao_cadastrar(e):
        nome_valor = nome.value.title().strip()
        email_valor = email.value.lower().strip()
        senha_valor = senha.value.strip()

        sucesso, resultado = UserManager.validar_campos_cadastro(nome_valor, email_valor, senha_valor)

        if sucesso:
            nome_msg.visible = False
            email_msg.visible = False
            senha_msg.visible = False
            confirmacao_senha_msg.visible = False
            geral_msg.visible = False
            page.update()
            time.sleep(2)
            mostrar_codigo_verificacao_email(page, email_valor, nome_valor, senha_valor)
        else:
            geral_msg.value = resultado
            geral_msg.color = ft.Colors.BLUE_700
            geral_msg.visible = True
        page.update()


    headline = ft.Column([
        ft.Container(
            ft.Text("Cadastro", size=32, text_align="left", width=343, font_family="InstrumentSans SemiBold", color="#006A71"),
            padding=ft.padding.only(top=50),
        ),
        ft.Text("Preencha suas informações abaixo para começar a aprender!", text_align="left", font_family="InstrumentSans Medium", width=343, size=20, color="#898989",
            style=ft.TextStyle(height=1.4)),
        
], horizontal_alignment="center", alignment="center", spacing=6)

    forms = ft.Column(
        [
            ft.Container(
                content=headline,
                padding=ft.padding.only(bottom=20)
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Nome", text_align="left", width=343, size=18, font_family="InstrumentSans Medium", color="#636262"),
                    container_nome,
                    ft.Container(padding=ft.padding.only(top=4), width=343, content=nome_msg)
                ], alignment="center", horizontal_alignment="center", spacing=7)
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Email", text_align="left", width=343, size=18, font_family="InstrumentSans Medium", color="#636262"),
                    container_email,
                    ft.Container(padding=ft.padding.only(top=4), width=343, content=email_msg)
                ], alignment="center", horizontal_alignment="center", spacing=7)
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Senha", text_align="left", width=343, size=18, font_family="InstrumentSans Medium", color="#636262"),
                    container_senha,
                    ft.Container(padding=ft.padding.only(top=4), width=343, content=senha_msg)
                ], alignment="center", horizontal_alignment="center", spacing=7)
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Confirmação de Senha", text_align="left", width=343, size=18, font_family="InstrumentSans Medium", color="#636262"),
                    container_confirmacao_senha,
                    ft.Container(padding=ft.padding.only(top=4), width=343, content=confirmacao_senha_msg)
                ], alignment="center", horizontal_alignment="center", spacing=7)
            ),
            ft.Container(
                content=ft.ElevatedButton("Continuar", style=ft.ButtonStyle(bgcolor="#01C6D3", overlay_color="#0ED2E0", color="white", shape=ft.RoundedRectangleBorder(radius=10), shadow_color="transparent", text_style=ft.TextStyle(font_family="InstrumentSans Medium", size=20, color="white")), width=343, height=50, on_click=ao_cadastrar),
                padding=ft.padding.only(top=20, bottom=20)
            ),
            geral_msg
        ],
        alignment="top",
        horizontal_alignment="center",
        spacing=20,
        width=400,
        scroll="auto",
        expand_loose=True
    )

    return forms