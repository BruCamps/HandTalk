import flet as ft
from core.user import User
from db.database import conectar

class QuizSession:
    def __init__(
        self, user: User, perguntas: list, 
        trilha: str = None, capitulo: str = None
    ):
        self.user = user
        self.perguntas = perguntas.copy()
        self.trilha = trilha
        self.capitulo = capitulo
        self.pergunta_atual = 0
        self.quizs_concluidos = 0
        self.vidas_restantes = 3
        self.respostas_certas = 0
        self.respostas_erradas = 0
        self.perguntas_puladas = []

    def responder(self, index):
        pergunta = self.perguntas[self.pergunta_atual]
        correta = index == pergunta["correta"]
        explicacao = pergunta["explicacao"]

        if correta:
            self.respostas_certas += 1
        else:
            self.vidas_restantes -= 1
            self.respostas_erradas += 1

        self.pergunta_atual += 1
        return correta, explicacao

    def pular(self):
        self.perguntas_puladas.append(self.perguntas[self.pergunta_atual])
        self.pergunta_atual += 1
        self.perguntas.extend(self.perguntas_puladas)
        self.perguntas_puladas = []

    def registrar_conclusao(self):
        if self.trilha and self.capitulo:
            if self.trilha not in self.user.progresso:
                self.user.progresso[self.trilha] = {}

            self.user.progresso[self.trilha][self.capitulo] = True

            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO progresso (user_id, trilha, capitulo, concluido)
                VALUES (?, ?, ?, ?)
            """, (self.user.id, self.trilha, self.capitulo, 1))
            conn.commit()
            conn.close()

    def terminou(self):
        return self.pergunta_atual >= len(self.perguntas) or self.vidas_restantes <= 0

    def calcular_xp(self):
        xp = self.respostas_certas * 10
        if self.respostas_certas == len(self.perguntas):
            xp *= 2
        self.user.xp += xp
        return xp

    def quantidade_quiz_concluidos(self):
        self.quizs_concluidos += 1
        return self.quizs_concluidos