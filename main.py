import flet as ft
from telas.login import mostrar_login
from telas.cadastro import mostrar_cadastro
from db.database import inicializar_db
from telas.tabs import mostrar_tabs

def main(page: ft.Page):
    page.bgcolor = "#FFFFFF"
    page.window.width = 412
    page.window.height = 917
    page.window.resizable = True
    page.window.left = 1000

    page.fonts = {
        "InstrumentSans": "fonts/InstrumentSans-Regular.ttf",
        "InstrumentSans Medium": "fonts/InstrumentSans-Medium.ttf",
        "InstrumentSans SemiBold": "fonts/InstrumentSans-SemiBold.ttf",
        "InstrumentSans Bold": "fonts/InstrumentSans-Bold.ttf",
        "InstrumentSans BoldItalic": "fonts/InstrumentSans-BoldItalic.ttf",
    }
    page.theme = ft.Theme(font_family="InstrumentSans")
  
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
 
    mostrar_tabs(page)
    
   
if __name__ == "__main__":
    inicializar_db()
    ft.app(target=main, name="HandTalk")