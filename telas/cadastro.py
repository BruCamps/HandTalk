import flet as ft
import time
from components.icons import *
from utils.funcoes import *
from components.entradas import *
from components.mensagens import *
from core.user_manager import UserManager
from core.customTexts import *
from core.customContainers import *
from core.customButtons import *
from telas.verificacao_codigo import mostrar_codigo_verificacao_email

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

    nome.on_change = lambda e: validar_nome(page, nome, container_nome, nome_msg, icon_name, icon_red_name)
    email.on_change = lambda e: validar_email(page, email, container_email, email_msg, icon_mail, icon_red_mail)
    senha.on_change = lambda e: validar_senha(page, senha, container_senha, senha_msg, icon_eyeoff_senha, icon_eyeon_senha, icon_red_eyeoff_senha, icon_red_eyeon_senha)
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

    forms = ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            content=Heading("Cadastro"), 
                            padding=ft.padding.only(top=50)
                        ),
                        SubHeading(
                            text="Preencha suas informações abaixo para começar a aprender!", 
                            style=ft.TextStyle(height=1.4)
                        )
                    ], 
                    horizontal_alignment="center", alignment="center", spacing=6
                ), 
                padding=ft.padding.only(bottom=20)
            ),
            ft.Container(
                ft.Column(
                    [
                        InputLabel("Nome"), 
                        container_nome, 
                        MessageContainer(content=nome_msg)
                    ], 
                    alignment="center", horizontal_alignment="center", spacing=7
                )
            ),
            ft.Container(
                ft.Column(
                    [
                        InputLabel("Email"), 
                        container_email, 
                        MessageContainer(content=email_msg)
                    ], 
                    alignment="center", horizontal_alignment="center", spacing=7
                )
            ),
            ft.Container(
                ft.Column(
                    [
                        InputLabel("Senha"), 
                        container_senha, 
                        MessageContainer(content=senha_msg)
                    ], 
                    alignment="center", horizontal_alignment="center", spacing=7
                )
            ),
            ft.Container(
                ft.Column(
                    [
                        InputLabel("Confirmação de Senha"), 
                        container_confirmacao_senha, 
                        MessageContainer(content=confirmacao_senha_msg)
                    ],
                    alignment="center", horizontal_alignment="center", spacing=7
                )
            ),
            PrimaryButton(
                text="Cadastrar", 
                on_click=ao_cadastrar
            ),
            MessageContainer(content=geral_msg)
        ],
        alignment="top", horizontal_alignment="center", spacing=20, width=400, 
        scroll="auto", expand_loose=True
    )

    return forms