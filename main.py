from database import criar_tabela
from utils.menu import exibir_menu
from services.biblioteca_service import (
	cadastrar_livro,
	listar_livros,
	buscar_livro_por_id,
	remover_livro,
	emprestar_livro,
	devolver_livro,
	atualizar_livro
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
		remover_livro()
	
	elif opcao == "5":
		atualizar_livro()

	elif opcao == "6":
		emprestar_livro()

	elif opcao == "7":
		devolver_livro()

	elif opcao == "0":
		print("\nEncerrando sistema...")
		break

	
	else:
		print("\nOpção inválida!")
