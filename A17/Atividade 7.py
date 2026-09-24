nome = input("Digite o nome do funcionário: ")
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor recebido por hora: R$ "))
horas_extras = float(input("Digite a quantidade de horas extras: "))
vale_transporte = input("Recebe vale-transporte? S ou N: ")

salario_base = horas_trabalhadas * valor_hora

valor_hora_extra = valor_hora * 1.5

total_horas_extras = horas_extras * valor_hora_extra

salario_bruto = salario_base + total_horas_extras

if salario_bruto <= 1500:
    inss = salario_bruto * 0.05
elif salario_bruto <= 3000:
    inss = salario_bruto * 0.08
else:
    inss = salario_bruto * 0.11

if vale_transporte == "S":
    desconto_vale = salario_base * 0.06
else:
    desconto_vale = 0

descontos = inss + desconto_vale

salario_liquido = salario_bruto - descontos

print("")
print("--- RESUMO DO SALÁRIO ---")
print("Nome:", nome)
print("Salário base:", salario_base)
print("Valor das horas extras:", total_horas_extras)
print("Salário bruto:", salario_bruto)
print("Desconto INSS:", inss)
print("Desconto vale-transporte:", desconto_vale)
print("Total de descontos:", descontos)
print("Salário líquido:", salario_liquido)