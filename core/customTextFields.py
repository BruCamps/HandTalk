import flet as ft

"""
    Classe utilizada para criar campos de entrada padronizados
"""
class CustomTextField(ft.TextField):
    def __init__(self, 
        suffix_icon, hint_text,  **kwargs
    ):
        super().__init__()
        self.suffix_icon = suffix_icon
        self.hint_text = hint_text
        self.content_padding = ft.padding.only(top=16, bottom=16, left=24)
        self.width = 343
        self.border="none"
        self.bgcolor="#E7F9FD"
        self.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 20}
        self.hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 20}
        self.hover_color="#E7F9FD"
        self.suffix_icon= suffix_icon
        self.overlay_color = ft.Colors.TRANSPARENT
        


"""
    Classe utilizada para criar campos de senha padronizados
"""
class PasswordTextField(ft.TextField):
    def __init__(self, 
        icon_regular_closed, hint_text, **kwargs
    ):
        super().__init__()
        self.hint_text = hint_text
        self.width = 343
        self.password = True
        self.max_length = 6
        self.can_reveal_password = True
        self.content_padding = ft.padding.only(top=16, bottom=16, left=24)
        self.border="none"
        self.show_password = False
        self.suffix_icon = icon_regular_closed
        self.overlay_color = ft.Colors.TRANSPARENT
        self.hover_color = ft.Colors.TRANSPARENT
        self.icon_regular_closed = icon_regular_closed
        self.bgcolor="#E7F9FD"
        self.text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "letter_spacing": 5, "size": 20}
        self.hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "letter_spacing": 0, "size": 20}
        self.icon_regular_opened = None
        self.icon_error_closed = None
        self.icon_error_opened = None
        self.validar_campo = None
        self.container = None
        self.msg_erro = ""
        self.campo_msg = None