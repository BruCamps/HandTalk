     
from core.user import User
from db.database import conectar
from telas.verificacao_codigo import gerar_codigo
import re
import flet as ft
from datetime import datetime

class UserManager:
    @staticmethod
    def cadastrar(nome, email, senha):
        conn = conectar()
        cursor = conn.cursor()
        senha_hash = User.gerar_hash_senha(senha)
        codigo = gerar_codigo()

        sucesso, mensagem = UserManager.validar_campos_cadastro(nome, email, senha)

        if not sucesso:
            conn.close()
            return False, mensagem

        try:
            cursor.execute("""
                INSERT INTO usuarios (nome, email, senha_hash, codigo_verificacao)
                VALUES (?, ?, ?, ?)
            """, (nome, email, senha_hash, codigo))
            conn.commit()
            return True, codigo
        except Exception as e:
            print(e)
            return False, "Email já cadastrado."
        finally:
            conn.close()

    @staticmethod
    def nome_valido(nome):
        nome = nome.strip()
        partes = nome.split()
        if len(partes) != 2: return False
        return all(re.match(r'^[A-Za-z]+$', parte) for parte in partes)

    @staticmethod
    def email_valido(email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@(gmail\.com|ufrpe\.br|outlook\.com|hotmail\.com)$', email.lower()) and not None

    @staticmethod
    def senha_valida(senha):
        return len(senha) >= 6 and not None

    @staticmethod
    def confirmacao_senha_valida(senha, confirmacao_senha):
        return senha == confirmacao_senha and not None

    @staticmethod
    def nova_senha_valida(senha, nova_senha):
        return senha != nova_senha

    @staticmethod
    def verificar_email(email, codigo):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo_verificacao FROM usuarios WHERE email = ?", (email,))
        resultado = cursor.fetchone()
        if resultado and resultado[0] == codigo:
            cursor.execute("UPDATE usuarios SET verificado = 1 WHERE email = ?", (email,))
            conn.commit()
            return True
        return False

    @staticmethod
    def login(email, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, nome, email, senha_hash, xp, streak FROM usuarios
            WHERE email = ? AND verificado = 1
        """, (email,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            user = User(*user_data)
            if user.verificar_senha(senha):
                return user
        return None

    @staticmethod
    def atualizar_xp(user: User):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET xp = ? WHERE id = ?", (user.xp, user.id))
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar_streak(user: User):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT MAX(data) FROM desempenho WHERE user_id = ?
        """, (user.id,))
        resultado = cursor.fetchone()

        hoje = datetime.now().date()
        ultimo_dia = resultado[0] if resultado else None

        if ultimo_dia:
            data_ultima = datetime.strptime(ultimo_dia, "%Y-%m-%d").date()
            diferenca = (hoje - data_ultima).days

            if diferenca == 0:
                pass
            elif diferenca == 1:
                user.streak += 1
            else:
                user.streak = 1
        else:
            user.streak = 1

        cursor.execute("UPDATE usuarios SET streak = ? WHERE id = ?", (user.streak, user.id))
        conn.commit()
        conn.close()

    @staticmethod
    def validar_campos_cadastro(nome, email, senha, confirmar_senha=None, nova_senha=None):
        if not nome or not email or not senha:
            return False, "Preencha todos os campos!"
        if not UserManager.nome_valido(nome):
            return False, ""

        elif not UserManager.email_valido(email):
            return False, ""

        elif not UserManager.senha_valida(senha):
            return False, ""

        elif confirmar_senha is not None and not UserManager.confirmacao_senha_valida(senha, confirmar_senha):
            return False, ""

        elif nova_senha is not None and not UserManager.nova_senha_valida(senha, nova_senha):
            return False, ""

        return True, ""


    
