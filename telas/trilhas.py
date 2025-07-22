import flet as ft
from components.icons import *
from core.menu import MenuNavegacao
from core.customContainers import *
from core.customButtons import *
from core.customTexts import *
from utils.perguntas import trilhas_disponiveis, perguntas_por_trilha

def get_capitulos_concluidos(trilha, user):
    capitulos = perguntas_por_trilha[trilha]["capitulos"]
    progresso = user.progresso.get(trilha, {})
    return sum(1 for nome in capitulos if progresso.get(nome))

def get_porcentagem_concluidos(trilha, user):
    total = len(perguntas_por_trilha[trilha]["capitulos"])
    concluidos = get_capitulos_concluidos(trilha, user)
    porcentagem_concluidos = int((concluidos / total) * 100)
    return porcentagem_concluidos

def get_proximo_capitulo(trilha, user):
    capitulos = perguntas_por_trilha[trilha]["capitulos"]
    progresso = user.progresso.get(trilha, {})
    for capitulo in capitulos:
        if not progresso.get(capitulo, False):
            return capitulo
    return list(capitulos.keys())[0]

def mostrar_trilhas(page: ft.Page, menu: MenuNavegacao):
    page.controls.clear()
    page.theme = ft.Theme(font_family="InstrumentSans")

    from core.state import estado
    from telas.quiz import iniciar_quiz

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

    cards = []

    for trilha in trilhas_disponiveis:
        trilha_data = perguntas_por_trilha[trilha]
        descricao = trilha_data["descrição"]
        total_capitulos = len(trilha_data["capitulos"])
        concluidos = get_capitulos_concluidos(trilha, estado.usuario_logado)
        porcentagem = get_porcentagem_concluidos(trilha, estado.usuario_logado)
        proximo_capitulo = get_proximo_capitulo(trilha, estado.usuario_logado)

        trilha_card = ContainerSection(
            content=ft.Column([
                ft.Column([
                    Paragraph(text=trilha[:7], color="#006A71"),
                    Paragraph(text=trilha[9:], color="#006A71", font_family="InstrumentSans Bold", size=20),
                ], spacing=2),
                ft.Row([
                    Paragraph(text="CAPÍTULO", size=16),
                    Paragraph(
                        text=f"{concluidos}/{total_capitulos}", color="#006A71", 
                        font_family="InstrumentSans SemiBold", size=16
                    )
                ], spacing=200),
                ProgressBarContainer(value=porcentagem / 100),
                Paragraph(text=descricao),
                PrimaryButton(
                    text="Iniciar", 
                    on_click=lambda e, t=trilha, c=proximo_capitulo: iniciar_quiz(
                        page, trilha=t, capitulo=c
                    )
                )
            ])
        ) 

        cards.append(trilha_card) 
    
    cards_row = ft.Column(cards, spacing=10, alignment="center", height=637, scroll="auto", expand_loose=True)
    page.add(cards_row)

    menu = MenuNavegacao(page)
    page.add(menu)
    menu.set_ativo("home")

    page.update()