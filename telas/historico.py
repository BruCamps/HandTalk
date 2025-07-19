import flet as ft
from db.database import conectar
from core.state import estado

def mostrar_historico(page: ft.Page):
    u = estado.usuario_logado
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT acertos, quizs_concluidos, data FROM desempenho WHERE user_id = ? ORDER BY data DESC", (u.id,))
    dados = cursor.fetchall()
    conn.close()

    page.controls.clear()
    page.add(ft.Text("Histórico de Quizzes", size=22, weight="bold"))

    if not dados:
        page.add(ft.Text("Nenhum quiz registrado."))
    else:
        for acertos, total, data in dados:
            percentual = round((acertos / total) * 100, 1) if total else 0
            page.add(ft.Text(f"Data: {data} | Acertos: {acertos}/{total} ({percentual}%)"))

    from telas.perfil import mostrar_perfil
    page.add(ft.TextButton("Voltar", on_click=lambda _: mostrar_perfil(page)))