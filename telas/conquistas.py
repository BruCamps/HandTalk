import flet as ft
from core.menu import MenuNavegacao

def mostrar_conquistas(page: ft.Page, menu: MenuNavegacao):
    page.controls.clear()
    page.theme = ft.Theme(font_family="InstrumentSans")

    menu = MenuNavegacao(page)

    page.add(
        ft.Container(
            content=ft.Text("Conquistas", size=22, font_family="InstrumentSans Bold", color="#006A71"),
            height=755, width=400, alignment=ft.alignment.center,
            padding=ft.padding.only(top=50, bottom=50),
        ),
        menu
    )

    menu.set_ativo("conquistas")
    page.update()