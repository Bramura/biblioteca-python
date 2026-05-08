from database import conectar
from models.livro import Livro

def cadastrar_livro():
	titulo = input("Título: ")
	autor = input("Autor: ")
	ano = int(input("Ano: "))

	conexao = conectar()
	cursor = conexao.cursor()

	cursor.execute("""
	INSERT INTO livros (titulo, autor, ano, disponivel)
	VALUES(?, ?, ?, ?)
	""", (titulo, autor, ano, True))

	conexao.commit()
	conexao.close()

	print("\nLivro cadastrado com sucesso!")


def listar_livros():
	conexao = conectar()
	cursor = conexao.cursor()

	cursor.execute("SELECT * FROM livros")

	livros = cursor.fetchall()

	conexao.close()

	if not livros:
		print("\nNenhum livro cadastrado.")
		return

	print("\n=== LISTA DE LIVROS ===\n")

	for livro in livros:
		livro_obj = Livro(
			id=livro[0],
			titulo=livro[1],
			autor=livro[2],
			ano=livro[3],
			disponivel=livro[4]
		)
		
		print(livro_obj)


def buscar_livro_por_id(id_livro):
	conexao = conectar()
	cursor = conexao.cursor()

	cursor.execute(
		"SELECT * FROM livros WHERE id = ?",
		(id_livro,)
	)

	livro = cursor.fetchone()

	conexao.close()

	if livro:
		return Livro(
			id=livro[0],
			titulo=livro[1],
			autor=livro[2],
			ano=livro[3],
			disponivel=livro[4]
		)
	
	return None

def remover_livro(id_livro):
	conexao = conectar()
	cursor = conexao.cursor()
	
	cursor.execute(
		"DELETE FROM livros WHERE id = ?",
		(id_livro,)
	)
	
	conexao.commit()
	conexao.close()

	print("\nLivro removido com sucesso!")

def emprestar_livro(id_livro):
	conexao = conectar()
	cursor = conexao.cursor()

	# verifica se existe e se está disponível
	cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
	resultado = cursor.fetchone()

	if not resultado:
		print("\nLivro não encontrado.")
		conexao.close()
		return

	if resultado[0] == 0:
		print("\nLivro já está emprestado.")
		conexao.close()
		return

	# atualiza status
	cursor.execute(
		"UPDATE livros SET disponivel = 0 WHERE id = ?",
		(id_livro,)
	)

	conexao.commit()
	conexao.close()

	print("\nLivro emprestado com sucesso!")

def devolver_livro(id_livro):
	conexao = conectar()
	cursor = conexao.cursor()

	cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
	resultado = cursor.fetchone()

	if not resultado:
		print("\nLivro não encontrado.")
		conexao.close()
		return

	if resultado[0] == 1:
		print("\nEste livro já está disponível.")
		conexao.close()
		return

	cursor.execute(
		"UPDATE livros SET disponivel = 1 WHERE id = ?", (id_livro,))

	conexao.commit()
	conexao.close()
	
	print("\nLivro devolvido com sucesso!")