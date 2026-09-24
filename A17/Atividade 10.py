nome = input("Digite o nome do consumidor: ")
consumo = float(input("Digite o consumo de água em m3: "))

print("1 - Residencial")
print("2 - Comercial")
tipo = int(input("Digite o tipo de imóvel: "))

if tipo == 1:
    if consumo <= 10:
        tarifa = 2
    elif consumo <= 20:
        tarifa = 3
    else:
        tarifa = 4.5
else:
    if consumo <= 10:
        tarifa = 3.5
    elif consumo <= 20:
        tarifa = 5
    else:
        tarifa = 7

valor_consumo = consumo * tarifa
taxa_servico = 12

if consumo > 30:
    multa = valor_consumo * 0.10
else:
    multa = 0

total = valor_consumo + taxa_servico + multa

if consumo <= 10:
    classificacao = "Baixo"
elif consumo <= 30:
    classificacao = "Moderado"
else:
    classificacao = "Elevado"

print("")
print("--- RESUMO DA CONTA ---")
print("Nome:", nome)
print("Consumo registrado:", consumo)
print("Tarifa utilizada:", tarifa)
print("Taxa de serviço:", taxa_servico)
print("Multa:", multa)
print("Classificação:", classificacao)
print("Valor total da conta:", total)