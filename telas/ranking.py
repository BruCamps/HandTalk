import flet as ft
from db.database import conectar
from core.menu import MenuNavegacao

def mostrar_ranking(page: ft.Page, menu: MenuNavegacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, xp FROM usuarios ORDER BY xp DESC LIMIT 5")
    top5 = cursor.fetchall()
    conn.close()

    page.controls.clear()
    page.theme = ft.Theme(font_family="InstrumentSans")

    from telas.trilhas import mostrar_trilhas

    menu = MenuNavegacao(page)

    page.add(
        *[
            ft.Container(
                content=ft.Column([
                    ft.Text("Ranking TOP 5", size=22, font_family="InstrumentSans Bold", color="#006A71"),
                    ft.Column([
                        ft.Text(f"{i}. {nome} - {xp} pontos", font_family="InstrumentSans SemiBold", color="#006A71",  size=18) 
                        for i, (nome, xp) in enumerate(top5, start=1)
                    ], spacing=5)
                ]), 
                height=755, width=400, alignment=ft.alignment.center,
                padding=ft.padding.only(top=50, bottom=50),
            ),
            menu
        ]
    )

    menu.set_ativo("ranking")

    page.update()