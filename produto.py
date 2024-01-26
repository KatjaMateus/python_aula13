class Produto:
    def __init__(self, nome:str, preco:float, qtd:int) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__qtd = qtd
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_nome):
        self.__nome = novo_nome
        return self.__nome
    
    def getPreco(self):
        return self.__preco
    
    def setPreco(self, novo_preco):
        if novo_preco < 0:
            print("Opção inválida")
        else:
            self.__preco = novo_preco
        return self.__preco
    
    def getQtd(self):
        return self.__qtd
    
    def setQtd(self, novo_qtd):
        if novo_qtd < 0:
            print("Opção inválida")
        else:
            self.__qtd = novo_qtd
        self.__qtd = novo_qtd
        return self.__qtd
    
produto1=(Produto(nome="banana", preco=4.50, qtd=5))
print(produto1.getPreco())
produto1.setPreco(5)
print(produto1.getPreco())
