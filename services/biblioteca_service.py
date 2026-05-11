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

def remover_livro():
	livro = selecionar_livro_por_id()

	conexao = conectar()
	cursor = conexao.cursor()
	
	cursor.execute(
		"DELETE FROM livros WHERE id = ?",
		(livro.id,)
	)
	
	conexao.commit()
	conexao.close()

	print("\nLivro removido com sucesso!")

def emprestar_livro():
	livro = selecionar_livro_por_id()

	if livro.disponivel == 0:
        	print("\nLivro já está emprestado.")
        	return

    	conexao = conectar()
    	cursor = conexao.cursor()

    	cursor.execute(
        	"UPDATE livros SET disponivel = 0 WHERE id = ?",
        	(livro.id,)
    	)

    	conexao.commit()
    	conexao.close()

    	print("\nLivro emprestado com sucesso!")

def devolver_livro(id_livro):
	livro = selecionar_livro_por_id()

	if livro.disponivel == 1:
        	print("\nLivro já está disponível.")
        	return

    	conexao = conectar()
    	cursor = conexao.cursor()

    	cursor.execute(
        	"UPDATE livros SET disponivel = 1 WHERE id = ?",
        	(livro.id,)
    	)

    	conexao.commit()
    	conexao.close()

    	print("\nLivro devolvido com sucesso!")

def selecionar_livro_por_id():
    	while True:
        	id_livro = int(input("\nDigite o ID do livro: "))

        	livro = buscar_livro_por_id(id_livro)

        	if not livro:
            	print("\nLivro não encontrado.")
            	continue

        	print("\nLivro encontrado:\n")
        	print(livro)

        	confirmacao = input("\nConfirmar livro? (y/n): ").lower()

        	if confirmacao == "y":
            	return livro

        	print("\nBuscando novamente...")

def atualizar_livro():
    	livro = selecionar_livro_por_id()

    	while True:
        	print("\n=== ATUALIZAR LIVRO ===")
        	print("1 - Título")
        	print("2 - Autor")
        	print("3 - Ano")
        	print("4 - Status de disponibilidade")
        	print("0 - Finalizar")

        	opcao = input("\nEscolha uma opção: ")

        	conexao = conectar()
        	cursor = conexao.cursor()

        	if opcao == "1":
            		novo_titulo = input("Novo título: ")

            		cursor.execute("""
            		UPDATE livros
            		SET titulo = ?
            		WHERE id = ?
            		""", (novo_titulo, livro.id))

            		print("\nTítulo atualizado com sucesso!")

        	elif opcao == "2":
            		novo_autor = input("Novo autor: ")

            		cursor.execute("""
            		UPDATE livros
            		SET autor = ?
            		WHERE id = ?
            		""", (novo_autor, livro.id))

            		print("\nAutor atualizado com sucesso!")

        	elif opcao == "3":
            		novo_ano = int(input("Novo ano: "))

            		cursor.execute("""
            		UPDATE livros
            		SET ano = ?
            		WHERE id = ?
            		""", (novo_ano, livro.id))

            		print("\nAno atualizado com sucesso!")

        	elif opcao == "4":
            		novo_status = int(input(
                	"Digite 1 para disponível ou 0 para emprestado: "
            	))

            		cursor.execute("""
            		UPDATE livros
            		SET disponivel = ?
            		WHERE id = ?
            		""", (novo_status, livro.id))

            		print("\nStatus atualizado com sucesso!")

        	elif opcao == "0":
            		conexao.close()
            		print("\nFinalizando atualização...")
            		break

        	else:
            		print("\nOpção inválida.")
            		conexao.close()
            		continue

        	conexao.commit()

		livro_atualizado = buscar_livro_por_id(livro.id)

		print("\n=== LIVRO ATUALIZADO ===\n")
		print(livro_atualizado)

        	conexao.close()