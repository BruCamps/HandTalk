import flet as ft


class PrimaryButton(ft.ElevatedButton):
    def __init__(
        self, text,
        style=ft.ButtonStyle(
            bgcolor="#01C6D3",
            overlay_color="#0ED2E0",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            shadow_color="transparent",
            text_style=ft.TextStyle(font_family="InstrumentSans Medium", size=20, color="white")
        ),
        width=343,
        height=50,
        on_click=None,
        **kwargs
    ):
        super().__init__()
        self.text = text
        self.style = style
        self.width = width
        self.height = height
        self.on_click = on_click

class TransparentButton(ft.ElevatedButton):
    def __init__(
        self, text=None, content=None,
        overlay_color="transparent",
        style=ft.ButtonStyle(
            overlay_color="transparent",
            shape=ft.RoundedRectangleBorder(radius=10),
            shadow_color="transparent",
            text_style=ft.TextStyle(
                font_family="InstrumentSans Medium", 
                size=20, 
                color="#01C6D3"
            ),
            surface_tint_color="transparent"
        ),
        padding=ft.padding.only(top=10, bottom=10),
        bgcolor="transparent",
        width=150,
        height=50,
        on_click=None,
        **kwargs
    ):
        super().__init__()
        self.text = text
        self.content = content
        self.overlay_color = overlay_color
        self.style = style
        self.padding = padding
        self.bgcolor = bgcolor
        self.width = width
        self.height = height
        self.on_click = on_click