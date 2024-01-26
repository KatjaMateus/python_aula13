class Aluno:
    def __init__(self, nome, idade, matricula) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula
    
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
    
    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, novo_valor):
        self.__matricula = novo_valor
        return self.__matricula
    
    def ver_infos(self):
         return f"""
        Informações de Aluno:
        Nome: {self.getNome()}
        Idade: {self.getIdade()}
        Matrícula: {self.getMatricula()}
        """
    
aluno1 = Aluno(nome="Maria", idade=25, matricula=345)

print(aluno1.getNome())
aluno1.setNome("Diana")
print(aluno1.getNome())
print(aluno1.ver_infos())

