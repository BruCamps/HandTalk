import sqlite3

def conectar():
    return sqlite3.connect("handtalk.db")
 
def inicializar_db():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha_hash TEXT NOT NULL,
            codigo_verificacao TEXT,
            verificado INTEGER DEFAULT 0,
            xp INTEGER DEFAULT 0,
            streak INTEGER DEFAULT 0,
            imagem_perfil BLOB
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS desempenho (
            user_id INTEGER,
            data TEXT,
            quizs_concluidos INTEGER DEFAULT 0,
            total_perguntas INTEGER DEFAULT 0,
            acertos INTEGER DEFAULT 0,
            erros INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, data)
        )
    ''')

    conn.commit()
    conn.close()