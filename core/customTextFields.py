import flet as ft

"""
    Classe utilizada para criar campos de entrada padronizados
"""
class CustomTextField(ft.TextField):
    def __init__(self, 
        suffix_icon, hint_text,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20}, 
        text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20},
        bgcolor="#E7F9FD", border="none", enable_suggestions=True, hover_color="#E7F9FD",
        content_padding=ft.padding.only(top=16, bottom=16, left=24), width=343, **kwargs
    ):
        super().__init__()
        self.suffix_icon = suffix_icon
        self.hint_style = hint_style
        self.hint_text = hint_text
        self.text_style = text_style
        self.bgcolor = bgcolor
        self.border = border
        self.enable_suggestions = enable_suggestions
        self.hover_color = hover_color
        self.content_padding = content_padding
        self.width = width


"""
    Classe utilizada para criar campos de senha padronizados
"""
class PasswordTextField(ft.TextField):
    def __init__(self, 
        suffix_icon, hint_text,
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}, 
        text_style={"color": "#006A71", "font_family": "InstrumentSans Bold", "letter_spacing": 5, "size": 20},
        bgcolor="#E7F9FD", border="none", width=343, hover_color="#E7F9FD",
        password=True, max_length=6, can_reveal_password=True, 
        content_padding=ft.padding.only(top=16, bottom=16, left=24), **kwargs
    ):
        super().__init__()
        self.suffix_icon = suffix_icon
        self.hint_style = hint_style
        self.hint_text = hint_text
        self.text_style = text_style
        self.bgcolor = bgcolor
        self.border = border
        self.width = width
        self.hover_color = hover_color
        self.password = password
        self.max_length = max_length
        self.can_reveal_password = can_reveal_password
        self.content_padding = content_padding