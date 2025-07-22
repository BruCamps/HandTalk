import flet as ft


"""
    Classe utilizada para criar mensagens de feedback
"""
class Message(ft.Text):
    def __init__(
        self, text="", color="red", size=14, 
        font_family="InstrumentSans SemiBold", 
        width=343, visible=False, **kwargs
    ):
        super().__init__()
        self.text = text
        self.color = color
        self.font_family = font_family
        self.size = size
        self.width = width
        self.visible = visible

class InputLabel(ft.Text):
    def __init__(
        self, text, text_align="left", size=18,
        color="#636262", font_family="InstrumentSans Medium", 
        width=343, **kwargs
    ):
        super().__init__()
        self.value = text
        self.text_align = text_align
        self.color = color
        self.font_family = font_family
        self.size = size
        self.width = width

class Heading(ft.Text):
    def __init__(self, 
        text, 
        text_align="left",
        color="#006A71", font_family="InstrumentSans SemiBold", 
        size=32, width=343, **kwargs
    ):
        super().__init__()
        self.value = text
        self.text_align = text_align
        self.color = color
        self.font_family = font_family
        self.size = size
        self.width = width

class TabText(ft.Text):
    def __init__(self, 
        text, 
        style=ft.TextStyle(color="#898989", font_family="InstrumentSans", size=20),
        animate_opacity=True, animate_offset=True, **kwargs
    ):
        super().__init__()
        self.value = text
        self.style = style
        self.animate_opacity = animate_opacity
        self.animate_offset = animate_offset

class SubHeading(ft.Text):
    def __init__(self, 
        text, 
        text_align="left",
        color="#898989", font_family="InstrumentSans Medium", 
        size=20, width=343, **kwargs
    ):
        super().__init__()
        self.value = text
        self.text_align = text_align
        self.color = color
        self.font_family = font_family
        self.size = size
        self.width = width

class UnderlinedText(ft.Text):
    def __init__(self, 
        text, 
        text_align="right", color="#009099", 
        font_family="InstrumentSans Medium", 
        size=16, width=343, 
        style=ft.TextStyle(
            decoration=ft.TextDecoration.UNDERLINE,  
            decoration_style=ft.TextDecorationStyle.SOLID, 
            decoration_thickness=2,
            decoration_color="#01C6D3"
        ),
        **kwargs
    ):
        super().__init__()
        self.value = text
        self.text_align = text_align
        self.color = color
        self.font_family = font_family
        self.size = size
        self.width = width
        self.style = style

class StatisticValue(ft.Text):
    def __init__(
        self, text, color="#006A71", 
        font_family="InstrumentSans Bold", 
        size=20, **kwargs
    ):
        super().__init__()
        self.value = text
        self.color = color
        self.font_family = font_family
        self.size = size

class StatisticText(ft.Text):
    def __init__(
        self, text, color="#AEAEAE", 
        font_family="InstrumentSans SemiBold", 
        size=16, **kwargs
    ):
        super().__init__()
        self.value = text
        self.color = color
        self.font_family = font_family
        self.size = size

class Paragraph(ft.Text):
    def __init__(
        self, text, color="#49999F", 
        font_family="InstrumentSans Medium", 
        size=14, **kwargs
    ):
        super().__init__()
        self.value = text
        self.color = color
        self.font_family = font_family
        self.size = size