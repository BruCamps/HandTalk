import flet as ft
from core.customTexts import *

def mostrar_tabs(page: ft.Page):
    page.controls.clear()
    
    def tab_changed(e):
        if e.control.selected_index == 0:
            tab_entrar.style = ft.TextStyle(color="#049FA9", font_family="InstrumentSans SemiBold", size=20)
            tab_cadastrar.style = ft.TextStyle(color="#898989", font_family="InstrumentSans", size=20)
        else:
            tab_entrar.style = ft.TextStyle(color="#898989", font_family="InstrumentSans", size=20)
            tab_cadastrar.style = ft.TextStyle(color="#049FA9", font_family="InstrumentSans SemiBold", size=20)
        page.update()

    tab_entrar = TabText(text="Entrar", style=ft.TextStyle(color="#049FA9", font_family="InstrumentSans SemiBold", size=20))
    tab_cadastrar = TabText(text="Cadastrar")
    
    from telas.login import mostrar_login
    from telas.cadastro import mostrar_cadastro

    tabs = ft.Tabs(
        selected_index=0,
        on_change=tab_changed,
        tabs=[
            ft.Tab(tab_content=tab_entrar, content=mostrar_login(page)),
            ft.Tab(tab_content=tab_cadastrar, content=mostrar_cadastro(page)),
        ],
        expand=True, width=400, overlay_color="#EEFCFF", 
        animation_duration=500, animate_opacity=True, animate_offset=True, 
        divider_color="transparent", indicator_color="#049FA9",
        label_text_style={
            "font_family": "InstrumentSans SemiBold", 
            "size": 20, 
            "color": "#898989"
        }
    )

    page.add(tabs)