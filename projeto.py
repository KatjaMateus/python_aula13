contador_id_livro = 1
contador_id_membro = 1

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor   
        self.status = True

class Membro:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.registro_membros = []
    

    def adicionar_livro(self):
        global contador_id_livro
        titulo_do_livro = input("Digite o título do livro: ")
        autor_do_livro = input("Digite o nome do autor: ")
        livro = Livro(titulo=titulo_do_livro,autor=autor_do_livro,id=contador_id_livro)
        contador_id_livro += 1
        self.catalogo_livros.append(livro)
        return "Livro adicionado com sucesso"


    def adicionar_membro(self):
        global contador_id_membro
        nome_do_membro = input("Digite o nome do novo membro: ")
        membro = Membro(nome=nome_do_membro, id=contador_id_membro)
        contador_id_membro += 1
        self.registro_membros.append(membro)
        return "Membro adicionado com sucesso"

    def pegar_emprestado(self):
        membro_nome = str(input("Digite o nome do membro: "))
        for membro in self.registro_membros:
            if membro_nome == membro.nome:
                livro_titulo = input("Digite o título do livro: ")
                for livro in self.catalogo_livros:
                    if livro_titulo == livro.titulo:
                        livro.status = False
                        membro.historico.append(livro)
                        return f"Livro {livro.titulo} emprestado "
                    else:
                        print("Livro não encontrado")
            else:
                return "Membro não encontrado. Por favor, cadastre o novo membro."


    
    def devolver_livro(self):
        livro_titulo = input("Digite o título do livro a devolver: ")
        for livro in self.catalogo_livros:
            if livro_titulo == livro.titulo:
                livro.status = True
                return f"Livro {livro.titulo} devolvido"
            else:
                print ("O livro não tem cadastro na nossa biblioteca")

    def pesquisar_livro(self):
        menu = int(input("""Escolha uma opção: 
                        1 - Pesquisar por título
                        2 - Pesquisar por autor
                        3 - Pesquisar por ID
                        """))
        if menu == 1:
            titulo = input("Digite o título do livro: ")
            for livro in self.catalogo_livros:
                if titulo == livro.titulo:
                    return f""" Informações do livro pesquisado
                        Título: {livro.titulo}
                        Autor: {livro.autor}
                        Id: {livro.id}
                        Status: {livro.status}
                        """
                else:
                    print("Livro não encontrado")
        elif menu == 2:
            autor = input("Digite o nome do autor: ")
            for livro in self.catalogo_livros:
                if autor == livro.autor:
                    return f"""Informações do livro pesquisado
                        Título: {livro.titulo}
                        Autor: {livro.autor}
                        Id: {livro.id}
                        Status: {livro.status}
                        """
                else:
                    print("Livro não encontrado")
        elif menu == 3:
            id = int(input("Digite o ID do livro: "))
            for livro in self.catalogo_livros:
                if id == livro.id:
                    return f"""Informações do livro pesquisado
                        Título: {livro.titulo}
                        Autor: {livro.autor}
                        Id: {livro.id}
                        Status: {livro.status}
                        """
                else:
                    print("Livro não encontrado")


biblioteca1 = Biblioteca()

while True:
    menu = int(input("""Escolha uma opção:
                    1 - Adicionar livro
                    2 - Adicionar membro
                    3 - Pesquisar livro
                    4 - Pegar livro emprestado
                    5 - Devolver livro
                    0 - Sair
                    """))
    if menu == 1:
        print(biblioteca1.adicionar_livro())
    elif menu == 2:
        print(biblioteca1.adicionar_membro())
    elif menu == 3:
        print(biblioteca1.pesquisar_livro())
    elif menu == 4:
        print(biblioteca1.pegar_emprestado())
    elif menu == 5:
        print(biblioteca1.devolver_livro())
    elif menu == 0:
        break
    else:
        print("Opção inválida")






