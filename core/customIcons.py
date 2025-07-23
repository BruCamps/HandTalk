import flet as ft

class Icon(ft.Image):
    def __init__(self, src_icon, width=22, height=22, **kwargs):
        super().__init__()
        self.src = src_icon
        self.width = width
        self.height = height

class ButtonIcon(ft.IconButton):
    def __init__(
        self, src_icon, width=22, height=22, highlight_color="#E0F1F5",
        on_click=None, **kwargs
    ):
        super().__init__()
        self.content = ft.Image(src=src_icon)
        self.width = width
        self.height = height
        self.highlight_color = highlight_color
        self.on_click = on_click

class ButtonIconRed(ft.IconButton):
    def __init__(
        self, src_icon, width=22, height=22, highlight_color="#FFEAEA",
        on_click=None, **kwargs
    ):
        super().__init__()
        self.content = ft.Image(src=src_icon)
        self.width = width
        self.height = height
        self.highlight_color = highlight_color
        self.on_click = on_click