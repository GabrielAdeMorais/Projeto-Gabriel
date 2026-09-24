#Solicitação das informações
placvei = str (input("Informe a placa do veículo: "))
horas = float (input("Informe quanto tempo o veículo ficou estacionado: "))



#Estrutura de repetição para verificar se o número é menor que 0
while horas < 0:
    horas = float(input("Valor inválido, informe as horas novamente: "))

#If usado para calcular o preço do estacionamento
if horas <= 1:
    valor = 8.00
elif horas > 1 and horas <= 3:
    valor = 15.00
elif horas > 3 and horas <= 6:
    valor = 25.00
else:
    valor = 40.00

print ("Você possui cadastro?")
cadastro = input("Selecione somente SIM ou NAO: ")

while cadastro.lower() not in ["sim", "nao"]:
    cadastro = input("Selecione somente SIM ou NAO: ")

if cadastro.lower() == "sim":
    desconto = (valor * 10)/100
    valorFinal = valor - desconto
else:
    print("Você não possui cadastro!")
    desconto = 0
    valorFinal = valor

#Relatório final
print("=" * 30)
print("          Relatório         ")
print("=" * 30)
print("")
print (f"Placa do veículo: {placvei}")
print (f"Tempo de permanência: {horas} horas.")
print (f"Valor original: R$ {valor}")
print (f"Valor do desconto: R$ {desconto}")
print (f"Valor final: R$ {valorFinal}")



