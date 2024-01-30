class bombaCombustivel:
    def __init__(self, tipoCombustivel: str, valorLitro: float, quantidadeCombustivel: int):
        self.tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def getValorLitro(self):
        return self.__valorLitro   
    
    def setValorLitro(self, novo_valor): 
        self.__valorLitro = novo_valor
        return self.__valorLitro
    
    def alterarValor(self,setValorLitro):
        novo_valor=setValorLitro(float(input("Digite o novo valor: ")))
        return novo_valor

    def abastecerPorValor(self,valor_abastecer,resultado_litros, total_litros):
        valor_abastecer= float(input("Digite o valor a ser abastecido: "))
        resultado_litros = valor_abastecer / self.getValorLitro()
        total_litros=self.quantidadeCombustivel-resultado_litros
        total_litros=self.quantidadeCombustivel
        return f"""O valor {valor_abastecer} deu {resultado_litros:.1} litros de combustível. 
        A quantidade atualizada de combustível na bomba é {total_litros}"""
    
    def abastecerPorLitro(self,quantidade_abastecer, resultado, total_litros):
        quantidade_abastecer= int(input("Digite o número de litros a ser abastecido: "))
        resultado = quantidade_abastecer * self.getValorLitro()
        total_litros=self.quantidadeCombustivel-quantidade_abastecer
        total_litros=self.quantidadeCombustivel
        return f"""O valor a pagar de {quantidade_abastecer} litros é {resultado} reais. 
        A quantidade atualizada de combustível na bomba é {total_litros}"""
    
        
bomba1=bombaCombustivel(tipoCombustivel="Etanol", valorLitro=4.99, quantidadeCombustivel=10000)
bomba2=bombaCombustivel(tipoCombustivel="Gasolina Comum", valorLitro=6.12, quantidadeCombustivel=10000)

#INTERFACE
menu = f"""Escolhe o tipo de combustível: 
            1 - Etanol
            2 - Gasolina Comum
            0 - Sair
    """
if menu == 1:
    escolha= f"""Escolhe uma opção: 
                1 - Abastecer por valor
                2 - Abastecer por litros
                3 - Alterar preço
                0 - Sair
            """
    if escolha == 1:
        bomba1.abastecerPorValor()
    elif escolha == 2:
        bomba1.abastecerPorLitro()
    elif escolha == 3:
        bomba1.alterarValor()
    elif escolha == 0:
        print("Programa encerrado")
    else:
        print("Opção inválida")
elif menu == 2:
    escolha= f"""Escolhe uma opção: 
                1 - Abastecer por valor
                2 - Abastecer por litros
                3 - Alterar preço
                0 - Sair
            """
    if escolha == 1:
        bomba2.abastecerPorValor()
    elif escolha == 2:
        bomba2.abastecerPorLitro()
    elif escolha == 3:
        bomba2.alterarValor()
    elif escolha == 0:
        print("Programa encerrado")
    else:
        print("Opção inválida")
elif menu == 0:
    print("Programa encerrado")
else:
    print("Opção inválida. Escolha um número válido")
        

    
    
    
    

