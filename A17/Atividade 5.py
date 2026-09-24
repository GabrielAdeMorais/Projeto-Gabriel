nome = input("Digite o nome do consumidor: ")
consumo = float(input("Digite o consumo mensal em kWh: "))

print("R - Residencial")
print("C - Comercial")
print("I - Industrial")
tipo = input("Digite o tipo de instalação: ")

if tipo == "R":
    if consumo <= 100:
        valor_consumo = consumo * 0.60
    else:
        valor_consumo = consumo * 0.75
elif tipo == "C":
    if consumo <= 100:
        valor_consumo = consumo * 0.70
    else:
        valor_consumo = consumo * 0.85
else:
    if consumo <= 100:
        valor_consumo = consumo * 0.80
    else:
        valor_consumo = consumo * 0.95

imposto = valor_consumo * 0.12
taxa = 15
total = valor_consumo + imposto + taxa

if consumo <= 100:
    classificacao = "Baixo"
elif consumo <= 250:
    classificacao = "Moderado"
else:
    classificacao = "Elevado"

print("")
print("--- RESUMO DA CONTA ---")
print("Nome:", nome)
print("Valor do consumo:", valor_consumo)
print("Imposto:", imposto)
print("Taxa fixa:", taxa)
print("Total:", total)
print("Classificação:", classificacao)