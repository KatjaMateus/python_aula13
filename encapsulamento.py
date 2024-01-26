class Pessoa:
    def __init__(self,nome: str, idade: int, altura: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_valor):
        self.__nome = novo_valor
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def setIdade(self, novo_valor):
        self.__idade = novo_valor
        return self.__idade
    
    def getAltura(self):
        return self.__altura
    
    def setAltura(self, novo_valor):
        self.__altura = novo_valor
        return self.__altura

    # def ver_infos(self):
    #     return f"""
    #     Informações da Pessoa:
    #     Nome: {self.nome}
    #     Idade: {self.idade}
    #     Altura: {self.altura}
    #     """
    
    def ver_infos(self):
        return f"""
        Informações da Pessoa:
        Nome: {self.getNome()}
        Idade: {self.getIdade()}
        Altura: {self.getAltura()}
        """

pessoa1 = Pessoa(nome="Maria", idade=25, altura=1.62)

print(pessoa1.getNome())
pessoa1.setNome("Ana")
print(pessoa1.getNome())
print(pessoa1.ver_infos())
# print(pessoa1.ver_infos())
# pessoa1.idade=90     #muda a idade

# print(pessoa1.ver_infos())
