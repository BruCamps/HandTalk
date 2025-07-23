import flet as ft
from core.state import estado
from core.user_manager import UserManager
from core.quiz import QuizSession
from db.database import conectar
from datetime import datetime
import core.menu as menu

def iniciar_quiz(page: ft.Page, trilha: str, capitulo: str):
    page.theme = ft.Theme(font_family="InstrumentSans")

    from utils.perguntas import perguntas_por_trilha
    perguntas = perguntas_por_trilha[trilha]["capitulos"][capitulo]["perguntas"]

    estado.sessao_quiz = QuizSession(estado.usuario_logado, perguntas, trilha, capitulo)

    mostrar_pergunta(page)

def mostrar_pergunta(page: ft.Page):
    quiz = estado.sessao_quiz

    if quiz.terminou():
        mostrar_resultado(page)
        return

    p = quiz.perguntas[quiz.pergunta_atual]
    explicacao = ft.Text("", size=16)

    def responder(e, index):
        correta, texto = quiz.responder(index)
        if correta:
            explicacao.value = "✅ Correto! " + texto
            explicacao.color = ft.Colors.GREEN
        else:
            explicacao.value = "❌ Incorreto. " + texto
            explicacao.color = ft.Colors.RED
        page.update()
        page.add(ft.ElevatedButton("Próxima", on_click=lambda _: mostrar_pergunta(page)))

    def pular(e):
        quiz.pular()
        mostrar_pergunta(page)

    page.controls.clear()
    page.add(
        ft.Text(f"Vidas restantes: {quiz.vidas_restantes}", size=16),
        ft.Text(p["enunciado"], size=20, weight="bold")
    )
    for i, alt in enumerate(p["alternativas"]):
        page.add(ft.ElevatedButton(text=alt, on_click=lambda e, idx=i: responder(e, idx)))
    page.add(ft.TextButton("Pular pergunta", on_click=pular), explicacao)
    page.update()

def mostrar_resultado(page: ft.Page):
    quiz = estado.sessao_quiz
    quiz.registrar_conclusao()
    xp = quiz.calcular_xp()
    quizs_concluidos = quiz.quantidade_quiz_concluidos()
    data_hoje = datetime.now().strftime("%Y-%m-%d")

    def finalizar_quiz(e):
        estado.sessao_quiz.registrar_conclusao()
        estado.sessao_quiz.calcular_xp()

        from telas.trilhas import mostrar_trilhas

        mostrar_trilhas(page, menu)

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO desempenho (user_id, data, quizs_concluidos, acertos, erros)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(user_id, data) DO UPDATE SET 
            quizs_concluidos = quizs_concluidos + ?,
            acertos = acertos + ?,
            erros = erros + ?
    """, (
        estado.usuario_logado.id,
        data_hoje,
        quizs_concluidos,
        quiz.respostas_certas,
        quiz.respostas_erradas,
        quizs_concluidos,
        quiz.respostas_certas,
        quiz.respostas_erradas
    ))
    cursor.execute("UPDATE usuarios SET xp = ? WHERE id = ?", (estado.usuario_logado.xp, estado.usuario_logado.id))
    conn.commit()
    conn.close()

    UserManager.atualizar_streak(estado.usuario_logado)

    from telas.trilhas import mostrar_trilhas
    import core.menu as menu

    page.controls.clear()
    page.add(
        ft.Text("Quiz finalizado!", size=24, weight="bold"),
        ft.Text(f"Você acertou {quiz.respostas_certas} de {len(quiz.perguntas)}.", size=18),
        ft.Text(f"XP conquistado: {xp}", size=18, color=ft.Colors.GREEN),
        ft.TextButton("Voltar ao menu", on_click=finalizar_quiz)
    )