class Livro:
	def __init__(self, titulo, autor, ano, disponivel=True, id=None):
		self.id = id
		self.titulo = titulo
		self.autor = autor
		self.ano = ano
		self.disponivel = disponivel

	def __str__(self):
		status = "Disponível" if self.disponivel else "Emprestado"

		return (
			f"ID: {self.id} | "
			f"Título: {self.titulo} | "
			f"Autor: {self.autor} | "
			f"Ano: {self.ano} | "
			f"Status: {status}"
		)