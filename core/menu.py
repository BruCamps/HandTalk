import flet as ft
from components.icons import *

class MenuNavegacao(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.icon_home = ft.Image(src=icon_home_filled, width=36, height=36)
        self.icon_ranking = ft.Image(src=icon_ranking_outlined, width=32, height=32)
        self.icon_conquistas = ft.Image(src=icon_conquistas_outlined, width=32, height=32)
        self.icon_perfil = ft.Image(src=icon_perfil_outlined, width=32, height=32)

        self.button_home = ft.ElevatedButton(content=self.icon_home, on_click=self.go_to_home, style=self.estilo())
        self.button_ranking = ft.ElevatedButton(content=self.icon_ranking, on_click=self.go_to_ranking, style=self.estilo())
        self.button_conquistas = ft.ElevatedButton(content=self.icon_conquistas, on_click=self.go_to_conquistas, style=self.estilo())
        self.button_perfil = ft.ElevatedButton(content=self.icon_perfil, on_click=self.go_to_perfil, style=self.estilo())

        self.content = ft.Row([self.button_home, self.button_ranking, self.button_conquistas, self.button_perfil],
                              spacing=20, height=50, alignment="center")
        self.padding = ft.padding.only(top=20, bottom=20)
        self.bgcolor = "#01C6D3"
        self.border_radius = 10
        self.width = 386

    def estilo(self):
        return ft.ButtonStyle(
            bgcolor="transparent", overlay_color="transparent", color="white",
            shape=ft.RoundedRectangleBorder(radius=10), shadow_color="transparent"
        )

    def set_ativo(self, ativo):
        self.icon_home.src = icon_home_filled if ativo == "home" else icon_home_outlined
        self.icon_home.width = 37 if ativo == "home" else 30
        self.icon_home.height = 37 if ativo == "home" else 30
        self.button_home.update()

        self.icon_ranking.src = icon_ranking_filled if ativo == "ranking" else icon_ranking_outlined
        self.icon_ranking.width = 37 if ativo == "ranking" else 32
        self.icon_ranking.height = 37 if ativo == "ranking" else 32
        self.button_ranking.update()

        self.icon_conquistas.src = icon_conquistas_filled if ativo == "conquistas" else icon_conquistas_outlined
        self.icon_conquistas.width = 37 if ativo == "conquistas" else 32
        self.icon_conquistas.height = 37 if ativo == "conquistas" else 32
        self.button_conquistas.update()

        self.icon_perfil.src = icon_perfil_filled if ativo == "perfil" else icon_perfil_outlined
        self.icon_perfil.width = 46 if ativo == "perfil" else 32
        self.icon_perfil.height = 46 if ativo == "perfil" else 32
        self.button_perfil.update()
        
        self.page.update()

    def go_to_home(self, e):
        from telas.trilhas import mostrar_trilhas
        self.set_ativo("home")
        mostrar_trilhas(self.page, self)

    def go_to_ranking(self, e):
        from telas.ranking import mostrar_ranking
        self.set_ativo("ranking")
        mostrar_ranking(self.page, self)

    def go_to_conquistas(self, e):
        from telas.conquistas import mostrar_conquistas
        self.set_ativo("conquistas")
        mostrar_conquistas(self.page, self)

    def go_to_perfil(self, e):
        from telas.perfil import mostrar_perfil
        self.set_ativo("perfil")
        mostrar_perfil(self.page, self)