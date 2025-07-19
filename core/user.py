import hashlib

class User:
    def __init__(self, user_id, nome, email, senha_hash, xp=0, streak=0):
        self.id = user_id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.xp = xp
        self.vida = 3
        self.streak = streak
        self.conquistas = []

    def verificar_senha(self, senha_digitada):
        return self.senha_hash == self.gerar_hash_senha(senha_digitada)

    @staticmethod
    def gerar_hash_senha(senha):
        return hashlib.sha256(senha.encode()).hexdigest()