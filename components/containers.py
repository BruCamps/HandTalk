import flet as ft
from core.state import estado
from components.icons import *
from core.customContainers import *
from core.customTexts import *
from db.database import conectar
from datetime import datetime, timedelta

u = estado.usuario_logado

container_pontos = StatisticsRow([
    icon_points,
    ColumnStatistics(
        [StatisticValue(f"{u.xp}"), StatisticText("Pontos")]
    )
])

container_streak = StatisticsRow([
    icon_streak,
    ColumnStatistics(
        [StatisticValue(f"{u.streak}"), StatisticText("Frequência")]
    )
])

conn = conectar()
cursor = conn.cursor()
cursor.execute("SELECT SUM(quizs_concluidos) FROM desempenho WHERE user_id = ?", (u.id,))
resultado_quiz = cursor.fetchone()
conn.close()

total_quizzes = resultado_quiz[0] if resultado_quiz and resultado_quiz[0] else 0

container_quiz = StatisticsRow([
    icon_book,
    ColumnStatistics(
        [StatisticValue(f"{total_quizzes}"), StatisticText("Quizzes")]
    )
])

container_emblema = StatisticsRow([
    icon_emblem,
    ColumnStatistics(
        [StatisticValue(f"{len(u.conquistas)}"), StatisticText("Conquistas")]
    )
])