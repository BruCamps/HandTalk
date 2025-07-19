import flet as ft
from src.components.icons import *
from core.menu import MenuNavegacao

def mostrar_trilhas(page: ft.Page, menu: MenuNavegacao):
    page.controls.clear()
    page.theme = ft.Theme(font_family="InstrumentSans")

    from utils.perguntas import trilhas_disponiveis
    trilhas = trilhas_disponiveis

    from core.state import estado

    u = estado.usuario_logado
    
    page.add(
        ft.Container(
            content=ft.Row([
                ft.Column([
                        ft.Text("Olá,", color="#006A71", font_family="InstrumentSans SemiBold", size=16),
                        ft.Text(estado.usuario_logado.nome, size=18, color="#006A71", font_family="InstrumentSans Bold"),
                ], width=220, alignment="center", horizontal_alignment="left", spacing=0),
                ft.Row([
                    ft.Row([
                        icon_points,
                        ft.Text(estado.usuario_logado.xp, color="#006A71", font_family="InstrumentSans SemiBold", size=16)
                    ], spacing=2, alignment="left"),
                    ft.Row([
                        icon_life_points,
                        ft.Text(estado.usuario_logado.vida, color="#006A71", font_family="InstrumentSans SemiBold", size=16)
                    ], spacing=2, alignment="center"),
                ], spacing=10, alignment="right")
            ], width=400, alignment="center"),
            width=400,
            padding=ft.padding.only(top=10, bottom=10, left=20, right=20),
        ),
        ft.Text("Escolha uma trilha para começar:", color="#006A71", font_family="InstrumentSans SemiBold", size=20)
    )

    from telas.quiz import iniciar_quiz
    page.add(
        ft.Column([
            ft.ElevatedButton(trilha, bgcolor="#006A71", color="white", on_click=lambda e, t=trilha: iniciar_quiz(page, trilha=t))
            for trilha in trilhas_disponiveis
            ], 
            spacing=10, alignment="center", height=637)
    )

    menu = MenuNavegacao(page)

    page.add(menu)

    menu.set_ativo("home")

    page.update()