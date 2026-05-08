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
	conexa = conectar()
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