#Função
def calcular_desconto(compra):
    if compra <= 100:
        return compra
    elif compra >= 500:
        return compra - (compra * 0.15)
    else:
        return compra - (compra * 0.10)


#Solicitação do valor da compra
compra = float(input("Digite o valor da compra: R$"))

#Valor final da compra com desconto
print(f"O valor final da compra é: R$ {calcular_desconto(compra)}")