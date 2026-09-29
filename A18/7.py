#Função
def calcular_total(produto,quantidade):
    valorFinal = float(produto) * int(quantidade)
    return valorFinal

#Solicitação do produto e quantidade
produto = input("Digite o valor do seu produto: R$")
quantidade = input("Digite a quantidade do seu produto: ")
#Valor final do produto
print(f"O valor final do seu produto é: R${calcular_total(produto,quantidade)}")

