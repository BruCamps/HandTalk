import flet as ft
from src.components.entradas import *
from src.components.icons import *
from src.components.utils.funcoes import *
from db.database import conectar
from core.state import estado
from telas.chart import gerar_grafico_minimalista
from PIL import Image
import base64
from core.menu import MenuNavegacao
from datetime import datetime
from collections import defaultdict
from telas.tabs import mostrar_tabs

def mostrar_perfil(page: ft.Page, menu: MenuNavegacao):
    page.theme = ft.Theme(font_family="InstrumentSans")
    mensagem = ft.Text("", text_align="center", size=18, font_family="InstrumentSans SemiBold", color="#006A71", visible=False)

    page.controls.clear()

    import core.menu as menu

    u = estado.usuario_logado
    nome_perfil.value = u.nome
    email_perfil.value = u.email

    # def salvar_dados(e):
    #     pass
    #     conn = conectar()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome_perfil.value, email_perfil.value, u.id))
    #         conn.commit()
    #         u.nome = nome_perfil.value
    #         u.email = email_perfil.value
    #         mensagem.value = "Dados atualizados com sucesso!"
    #         mensagem.color = ft.Colors.GREEN
    #     except:
    #         mensagem.value = "Erro ao atualizar dados."
    #         mensagem.color = ft.Colors.RED
    #     finally:
    #         conn.close()
    #     mostrar_perfil(page, menu)

    def sair(e):
        estado.usuario_logado = None
        email_login.value = ""
        senha_login.value = ""
        autenticar(page, email_login, senha_login, menu)
        mostrar_tabs(page)

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT acertos, erros, data FROM desempenho WHERE user_id = ?", (u.id,))
    resultados = cursor.fetchall()
    conn.close()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(quizs_concluidos) FROM desempenho WHERE user_id = ?", (u.id,))
    resultado_quiz = cursor.fetchone()
    conn.close()

    total_quizzes = resultado_quiz[0] if resultado_quiz and resultado_quiz[0] else 0

    # Organizar por dia da semana
    semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
    acertos_por_dia = defaultdict(int)
    erros_por_dia = defaultdict(int)

    for acertos, erros, data in resultados:
        dia_semana = datetime.strptime(data, "%Y-%m-%d").weekday()
        acertos_por_dia[dia_semana] += acertos
        erros_por_dia[dia_semana] += erros

    acertos_valores = [acertos_por_dia.get(i,0) for i in range(7)]
    erros_valores = [erros_por_dia.get(i,0) for i in range(7)]

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT imagem_perfil FROM usuarios WHERE id = ?", (u.id,))
    row = cursor.fetchone()
    conn.close()

    imagem_base64 = None
    if row and row[0] and isinstance(row[0], bytes):
        imagem_base64 = base64.b64encode(row[0]).decode('utf-8')

    grafico = gerar_grafico_minimalista(semana, acertos_valores, erros_valores)

    icon_points.width = 36
    icon_points.height = 36

    profile = ft.Stack([
        ft.Container(
            width=170, height=170, border_radius=170,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left, 
                end=ft.alignment.bottom_right, 
                colors=["#006A71", "#01C6D3"]
            )
        ),
        ft.Image(
            width=160, height=160,
            src_base64=imagem_base64 if imagem_base64 else None,
            src="src/assets/profile.svg" if not imagem_base64 else None,
            border_radius=160, fit="cover"
        )
    ], alignment=ft.alignment.center)

    container_pontos = ft.Row([
        icon_points,
        ft.Column([
            ft.Text(f"{u.xp}", size=20, font_family="InstrumentSans Bold", color="#006A71"),
            ft.Text("Pontos", size=16, font_family="InstrumentSans SemiBold", color="#AEAEAE"),
        ],
            alignment=ft.alignment.center,
            spacing=2
        )
    ], spacing=8, alignment=ft.alignment.center, width=150)

    container_streak = ft.Row([
        icon_streak,
        ft.Column([
            ft.Text(f"{u.streak}", size=20, font_family="InstrumentSans Bold", color="#006A71"),
            ft.Text("Frequência", size=16, font_family="InstrumentSans SemiBold", color="#AEAEAE"),
        ],
            alignment=ft.alignment.center,
            spacing=2
        )
    ], spacing=8, alignment=ft.alignment.center, width=150)

    container_quiz = ft.Row([
        icon_book,
        ft.Column([
            ft.Text(f"{total_quizzes}", size=20, font_family="InstrumentSans Bold", color="#006A71"),
            ft.Text("Conteúdos", size=16, font_family="InstrumentSans SemiBold", color="#AEAEAE"),
        ],
            alignment=ft.alignment.center,
            spacing=2
        )
    ], spacing=8, alignment=ft.alignment.center, width=150)

    container_emblema = ft.Row([
        icon_emblem,
        ft.Column([
            ft.Text(f"{len(u.conquistas)}", size=20, font_family="InstrumentSans Bold", color="#006A71"),
            ft.Text("Conquistas", size=16, font_family="InstrumentSans SemiBold", color="#AEAEAE"),
        ],
            alignment=ft.alignment.center,
            spacing=2
        )
    ], spacing=8, alignment=ft.alignment.center, width=150)

    from telas.editar_perfil import mostrar_tela_edicao_perfil
    
    page.controls.extend([
        ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=profile,
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=50)
                    ),
                    ft.Text(u.nome, text_align="center", size=24, font_family="InstrumentSans Bold", color="#006A71", width=343),
                    ft.Text(u.email, text_align="center", size=16, font_family="InstrumentSans Medium", color="#636262", width=343),
                    ft.Row([
                        ft.Container(
                        content=ft.ElevatedButton(
                            "Editar Perfil",
                            width=150, height=35,
                            style=ft.ButtonStyle(
                                bgcolor="#01C6D3", color="white", shape=ft.RoundedRectangleBorder(radius=8), 
                                shadow_color="transparent", overlay_color="#0ED2E0",
                                text_style=ft.TextStyle(font_family="InstrumentSans Medium", size=16, color="white")
                            ), on_click=lambda e: mostrar_tela_edicao_perfil(page, imagem_base64)),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Row([
                                    icon_logout,
                                    ft.Text("Sair", text_align="center", size=16, font_family="InstrumentSans Medium", color="#009099")
                                ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10), shadow_color="transparent", bgcolor="white",
                                    surface_tint_color="white", overlay_color="white", padding=ft.padding.only(top=10, bottom=10)
                                ), 
                                width=150,
                                height=35,
                                on_click=sair
                            ),
                            alignment=ft.alignment.center
                        )
                    ], alignment="center", spacing=10),
                    mensagem,
                    ft.Container(
                        content=ft.Text("Estatísticas", text_align="center", size=24, font_family="InstrumentSans SemiBold", color="#006A71"),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=25, bottom=25)
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Row(
                                [container_streak, container_quiz], 
                                spacing=40, alignment="center"
                            ),
                            ft.Row(
                                [container_emblema, container_pontos], 
                                spacing=40, alignment="center"
                            )
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text("Desempenho", text_align="center", size=24, font_family="InstrumentSans SemiBold", color="#006A71"),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=25)
                    ),
                    ft.Container(
                        content=ft.Text("Essa semana", text_align="center", size=16, font_family="InstrumentSans Medium", color="#AEAEAE"),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=10)
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Row(
                                [
                                    ft.Container( width=8, height=8,bgcolor="#01C6D3", border_radius=2),
                                    ft.Text("Acertos", size=16, font_family="InstrumentSans Medium", color="#006A71")
                                ], 
                                spacing=8, alignment="center"
                            ),
                            ft.Row(
                                [
                                    ft.Container(width=8, height=8,bgcolor="#F56A5F", border_radius=2),
                                    ft.Text("Erros", size=16, font_family="InstrumentSans Medium", color="#006A71")
                                ], 
                                spacing=8, alignment="center"
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                    ),
                    ft.Container(
                        content=ft.Image(
                            src_base64=grafico, fit="contain", width=400, height=145) if grafico else ft.Text("Nenhum quiz respondido ainda.", size=18, font_family="InstrumentSans Medium", color="#636262"),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(bottom=25)
                    )
                ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center
            )
        ], scroll="auto", height=755, expand_loose=True)
    ])

    menu = MenuNavegacao(page)
    page.add(menu)
    menu.set_ativo("perfil")
    page.update()