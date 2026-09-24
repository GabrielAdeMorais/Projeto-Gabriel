#Solicitação de informação
distancia = float(input("Digite a distância total da viagem em km: "))
consumo_medio = float(input("Digite o consumo médio do veículo em km/l: "))
litros_disponiveis = float(input("Digite a quantidade de litros disponíveis: "))
preco_litro = float(input("Digite o preço do litro do combustível: R$ "))
pedagio = input("A viagem inclui pedágio? S ou N: ")

#Calculo
litros_necessarios = distancia / consumo_medio
custo_combustivel = litros_necessarios * preco_litro

if pedagio == "S":
    quantidade_pedagios = int(input("Digite a quantidade de pedágios: "))
    valor_pedagio = float(input("Digite o valor médio de cada pedágio: R$ "))
    custo_pedagios = quantidade_pedagios * valor_pedagio
else:
    custo_pedagios = 0

custo_total = custo_combustivel + custo_pedagios

#If para saber se é suficiente ou insuficiente
if litros_disponiveis >= litros_necessarios:
    combustivel = "Suficiente"
    litros_restantes = litros_disponiveis - litros_necessarios
else:
    combustivel = "Insuficiente"
    litros_restantes = litros_necessarios - litros_disponiveis

#Resumo da viagem
print("")
print("--- RESUMO DA VIAGEM ---")
print("Litros necessários:", litros_necessarios)
print("Gasto com combustível:", custo_combustivel)
print("Gasto com pedágios:", custo_pedagios)
print("Custo total da viagem:", custo_total)
print("Combustível:", combustivel)

if litros_disponiveis >= litros_necessarios:
    print("Litros que sobrarão:", litros_restantes)
else:
    print("Litros que faltarão:", litros_restantes)