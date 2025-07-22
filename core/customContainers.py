import flet as ft

"""
    Classe utilizada para criar containers de entrada padronizados
"""
class InputContainer(ft.Container):
    def __init__(self, 
        content, 
        width=343, bgcolor="#E7F9FD", border_radius=15, 
        padding=ft.padding.only(right=8), 
        margin=ft.margin.only(bottom=16), 
        visible=True
    ):
        super().__init__()
        self.content = content
        self.width = width
        self.bgcolor = bgcolor
        self.border_radius = border_radius
        self.padding = padding
        self.margin = margin
        self.visible = visible

class MessageContainer(ft.Container):
    def __init__(self, 
        content, 
        padding=ft.padding.only(top=4), 
        width=343
    ):
        super().__init__()
        self.content = content
        self.padding = padding
        self.width = width

class StatisticsRow(ft.Row):
    def __init__(
        self, controls, 
        width=150, spacing=8,
        alignment=ft.alignment.center,
        **kwargs
    ):
        super().__init__()
        self.controls = controls
        self.width = width
        self.spacing = spacing
        self.alignment = alignment

class ColumnStatistics(ft.Column):
    def __init__(
        self, controls, 
        spacing=2,
        alignment=ft.alignment.center,
        **kwargs
    ):
        super().__init__()
        self.controls = controls
        self.spacing = spacing
        self.alignment = alignment

class ContainerSection(ft.Container):
    def __init__(
        self, 
        content, 
        width=400, bgcolor="#E7F9FD", border_radius=15, 
        padding=ft.padding.only(top=16, left=16, right=16, bottom=16), 
        margin=ft.margin.only(top=16, left=16, right=16), alignment=ft.alignment.center, **kwargs
    ):
        super().__init__()
        self.content = content
        self.width = width
        self.bgcolor = bgcolor
        self.border_radius = border_radius
        self.padding = padding
        self.margin = margin

class ProgressBarContainer(ft.ProgressBar):
    def __init__(
        self, value, 
        bgcolor="#A4E4E8", color="#01C6D3", 
        width=343, height=8, border_radius=10, **kwargs
    ):
        super().__init__()
        self.value = value
        self.bgcolor = bgcolor
        self.color = color
        self.width = width
        self.height = height
        self.border_radius = border_radius