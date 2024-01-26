class Autor:
    def __init__(self, nome: str, idade: int, nacionalidade: str):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo:str, autor:Autor, genero:str, qtde_paginas:int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qtde_paginas = qtde_paginas

autor1 = Autor(nome="João", idade=52, nacionalidade="brasileiro")
livro1 = Livro(titulo="Historias do João", autor=autor1, genero="drama", qtde_paginas=234)

print(livro1.titulo)
print(livro1.autor.nacionalidade)