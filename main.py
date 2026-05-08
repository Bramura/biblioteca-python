from database import criar_tabela
from utils.menu import exibir_menu
from services.biblioteca_service import (
	cadastrar_livro,
	listar_livros,
)

criar_tabela()

while True:
	exibir_menu()

	opcao = input("\nEscolha uma opção: ")

	if opcao == "1":
		cadastrar_livro()

	elif opcao == "2":
		listar_livros()

	elif opcao == "0":
		print("\nEncerrando sistema...")
		break

	
	else:
		print("\nOpção inválida!")
