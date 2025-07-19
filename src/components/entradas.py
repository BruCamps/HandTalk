import flet as ft
from src.components.icons import *
from src.components.utils.funcoes import *

ft.Theme(font_family="InstrumentSans")

nome = ft.TextField(
    bgcolor="#E7F9FD",
    border="none", 
    suffix_icon=icon_name,
    enable_suggestions=True,
    hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20},
    hint_text="Digite seu nome",
    text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20},
    width=343,
    content_padding=ft.padding.only(top=16, bottom=16, left=24)
)

email = ft.TextField(
        bgcolor="#E7F9FD",
        border="none", 
        suffix_icon=icon_mail,
        enable_suggestions=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20},
        hint_text="Digite seu email",
        text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20},
        width=343, 
        content_padding=ft.padding.only(top=16, bottom=16, left=24)
)

email_login = ft.TextField(
        bgcolor="#E7F9FD",
        border="none", 
        suffix_icon=icon_mail_login,
        enable_suggestions=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20},
        hint_text="Digite seu email",
        text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20},
        width=343, 
        content_padding=ft.padding.only(top=16, bottom=16, left=24)
)

email_recuperacao = ft.TextField(
        bgcolor="#E7F9FD",
        border="none", 
        suffix_icon=icon_mail_recuperacao,
        enable_suggestions=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20},
        hint_text="Digite seu email",
        text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20},
        width=343, 
        content_padding=ft.padding.only(top=16, bottom=16, left=24)
)

senha = ft.TextField(
        bgcolor="transparent", password=True, 
        max_length=6,
        border="none",
        hint_text="Digite sua senha",
        can_reveal_password=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20},
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        suffix_icon=icon_eyeoff_senha,
        content_padding=ft.padding.only(top=16, bottom=16, left=24),
        width=343
)

senha_login = ft.TextField(
        bgcolor="transparent", password=True, 
        max_length=6,
        border="none",
        hint_text="Digite sua senha",
        can_reveal_password=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20},
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        suffix_icon=icon_eyeoff_senha_login,
        content_padding=ft.padding.only(top=16, bottom=16, left=24),
        width=343
)

senha_nova_recuperacao = ft.TextField(
        bgcolor="transparent", password=True, 
        max_length=6,
        border="none",
        hint_text="Digite sua nova senha",
        can_reveal_password=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20},
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        suffix_icon=icon_eyeoff_senha_recuperacao,
        content_padding=ft.padding.only(top=16, bottom=16, left=24),
        width=343
)

confirmacao_senha_recuperacao = ft.TextField(
        bgcolor="transparent", password=True, 
        max_length=6,
        border="none",
        hint_text="Confirme sua nova senha",
        can_reveal_password=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20},
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        suffix_icon=icon_eyeoff_confirma_senha_recuperacao,
        content_padding=ft.padding.only(top=16, bottom=16, left=24),
        width=343
)

confirmacao_senha = ft.TextField(
        bgcolor="#E7F9FD", password=True, 
        max_length=6,
        border="none",
        hint_text="Confirme sua senha",
        can_reveal_password=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20},
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        suffix_icon=icon_eyeoff_confirma_senha,
        content_padding=ft.padding.only(top=16, bottom=16, left=24),
        width=343
)

nome_perfil = ft.TextField(
        bgcolor="#E7F9FD",
        border="none", 
        suffix_icon=icon_name,
        enable_suggestions=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20},
        hint_text="Digite seu nome",
        text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20},
        width=343,
        content_padding=ft.padding.only(top=16, bottom=16, left=24)
)

email_perfil = ft.TextField(
        bgcolor="#E7F9FD",
        border="none", 
        suffix_icon=icon_mail,
        enable_suggestions=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20},
        hint_text="Digite seu email",
        text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20},
        width=343, 
        content_padding=ft.padding.only(top=16, bottom=16, left=24)
)

senha_perfil = ft.TextField(
        bgcolor="#E7F9FD", password=True, 
        max_length=6,
        border="none",
        hint_text="Digite sua senha atual",
        can_reveal_password=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20},
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        suffix_icon=icon_eyeoff_senha_perfil,
        content_padding=ft.padding.only(top=16, bottom=16, left=24),
        width=343
)

senha_nova_perfil = ft.TextField(
        bgcolor="#E7F9FD", password=True, 
        max_length=6,
        border="none",
        hint_text="Digite sua nova senha",
        can_reveal_password=True,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20},
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        suffix_icon=icon_eyeoff_nova_senha_perfil,
        content_padding=ft.padding.only(top=16, bottom=16, left=24),
        width=343
)

container_nome = ft.Container(content=nome, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)
container_email = ft.Container(content=email, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)
container_senha = ft.Container(content=senha, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)
container_confirmacao_senha = ft.Container(content=confirmacao_senha, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)

container_email_login = ft.Container(content=email_login, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)
container_senha_login = ft.Container(content=senha_login, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)

container_nome_perfil = ft.Container(content=nome_perfil, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), margin=ft.margin.only(bottom=16), visible=True)
container_email_perfil = ft.Container(content=email_perfil, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), margin=ft.margin.only(bottom=16), visible=True)
container_senha_perfil = ft.Container(content=senha_perfil, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), margin=ft.margin.only(bottom=16), visible=True)
container_senha_nova_perfil = ft.Container(content=senha_nova_perfil, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), margin=ft.margin.only(bottom=16), visible=True)

container_recuperacao_email = ft.Container(content=email_recuperacao, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)
container_recuperacao_senha = ft.Container(content=senha_nova_recuperacao, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)
container_confirmacao_senha_recuperacao = ft.Container(content=confirmacao_senha_recuperacao, width=343, bgcolor="#E7F9FD", border_radius=15, padding=ft.padding.only(right=8), visible=True)
