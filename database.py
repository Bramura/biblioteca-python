import sqlite3

NOME_BANCO = "biblioteca.db"

def conectar():
	conexao = sqlite3.connect(NOME_BANCO)
	return conexao


def criar_tabela():
	conexao = conectar()
	cursor = conexao.cursor()
	
	cursor.execute("""
	CREATE TABLE IF NOT EXISTS livros (
        	id INTEGER PRIMARY KEY AUTOINCREMENT,
        	titulo TEXT NOT NULL,
        	autor TEXT NOT NULL,
        	ano INTEGER,
        	disponivel BOOLEAN NOT NULL DEFAULT 1
    	)
    	""")
	
	conexao.commit()
	conexao.close()