import flet as ft
import time

def mostrar_splash_screen(page: ft.Page):

    splash_screen = ft.Container(
        content=ft.Column(
            [
                ft.Column([
                    ft.Image(src="src/assets/logo-v1.png", width=100, height=100),
                    ft.Text("HandTalk", style=ft.TextStyle(font_family="InstrumentSans Bold", color="white", size=32)),
                    ft.Text("Por uma educação mais inclusiva", style=ft.TextStyle(font_family="InstrumentSans Medium", color="#C0D9DA", size=18))
                ], spacing=4, height=700, alignment="center", horizontal_alignment="center"),
                ft.Text("Made by HandTalk", style=ft.TextStyle(font_family="InstrumentSans", color="#C0D9DA", size=18))
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True,
        ),
        width=412,
        height=917,
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center, 
            end=ft.alignment.bottom_center, 
            colors=["#DAFF96", "#46A385", "#006A71"]
        )
    )

    page.overlay.append(splash_screen)
    page.update()
    time.sleep(3)
    page.overlay.remove(splash_screen)
    page.update()