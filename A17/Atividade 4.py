#Solicitação de informações
nome = input("Digite o nome do cliente: ")
valor_compra = float(input("Digite o valor da compra: R$ "))
peso = float(input("Digite o peso do pedido em kg: "))

print("1 - Região Metropolitana")
print("2 - Interior do estado")
print("3 - Outro estado")
regiao = int(input("Escolha a região: "))

print("1 - Entrega comum")
print("2 - Entrega expressa")
tipo_entrega = int(input("Escolha o tipo de entrega: "))

#If para atribuir valores a qual região o usuário escolher
if regiao == 1:
    frete = 12
    nome_regiao = "Região Metropolitana"
elif regiao == 2:
    frete = 20
    nome_regiao = "Interior do estado"
else:
    frete = 35
    nome_regiao = "Outro estado"

#If para atribuir o frete
if peso > 5:
    excesso = peso - 5
    frete = frete + excesso * 3

if tipo_entrega == 2:
    frete = frete + frete * 0.50
    nome_entrega = "Expressa"
else:
    nome_entrega = "Comum"

if valor_compra > 500:
    frete = frete - frete * 0.20

total = valor_compra + frete


#Resumo da compra com os valores finais
print("")
print("--- RESUMO DA COMPRA ---")
print("Cliente:", nome)
print("Valor da compra: R$",(valor_compra))
print("Peso do pedido:", peso, "kg")
print("Região:", nome_regiao)
print("Tipo de entrega:", nome_entrega)
print("Valor final do frete: R$",(frete))
print("Total da compra com frete: R$",(total))