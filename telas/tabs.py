import flet as ft
def mostrar_tabs(page: ft.Page):
    page.controls.clear()
    
    def tab_changed(e):
        if e.control.selected_index == 0:
            tab_entrar.color = "#049FA9"
            tab_entrar.font_family = "InstrumentSans SemiBold"
            tab_cadastrar.color = "#898989"
            tab_cadastrar.font_family = "InstrumentSans"
            page.update()
        else:
            tab_entrar.color = "#898989"
            tab_entrar.font_family = "InstrumentSans"
            tab_cadastrar.color = "#049FA9"
            tab_cadastrar.font_family = "InstrumentSans SemiBold"
            page.update()

    tab_entrar = ft.Text("Entrar", color="#049FA9", size=20, font_family="InstrumentSans SemiBold", animate_opacity=True, animate_offset=True)
    tab_cadastrar = ft.Text("Cadastrar", color="#898989", size=20, font_family="InstrumentSans", animate_opacity=True, animate_offset=True)
    
    from telas.login import mostrar_login
    from telas.cadastro import mostrar_cadastro

    tabs = ft.Tabs(
            selected_index=0,
            on_change=tab_changed,
            tabs=[
                ft.Tab(
                    tab_content=tab_entrar, 
                    content=mostrar_login(page)),
                ft.Tab(
                    tab_content=tab_cadastrar, 
                    content=mostrar_cadastro(page)),
            ],
            expand=True, animation_duration=500, animate_opacity=True, 
            animate_offset=True,
            divider_color="transparent",
            indicator_color="#049FA9",
            label_text_style={
                "weight": "semibold", "size": 20
            },
            label_color="#049FA9",
            width=400
    )

    page.add(tabs)