from database import criar_tabela
from utils.menu import exibir_menu
from services.biblioteca_service import (
	cadastrar_livro,
	listar_livros,
	buscar_livro_por_id,
	remover_livro,
	emprestar_livro,
	devolver_livro
)

criar_tabela()

while True:
	exibir_menu()

	opcao = input("\nEscolha uma opção: ")

	if opcao == "1":
		cadastrar_livro()

	elif opcao == "2":
		listar_livros()
	
	elif opcao == "3":
		id_livro = int(input("Digite o ID do livro: "))

		livro = buscar_livro_por_id(id_livro)

		if livro:
			print("\nLivro encontrado:\n")
			print(livro)
		else:
			print("\nLivro não encontrado.")

	elif opcao == "4":
		id_livro = int(input("Digite o ID do livro: "))
		remover_livro(id_livro)

	elif opcao == "5":
		id_livro = int(input("Digite o ID do livro: "))
		emprestar_livro(id_livro)

	elif opcao == "6":
		id_livro = int(input("Digite o ID do livro: "))
		devolver_livro(id_livro)

	elif opcao == "0":
		print("\nEncerrando sistema...")
		break

	
	else:
		print("\nOpção inválida!")
