#Versão 1 / valor = valor / divisor
valor = 675.00
divisor = 5
desconto = 15.00

print (f"Valor inicial: R${valor}")
valor = valor / divisor
print(f"Valor para cada colega: R${valor}")
valor = valor - desconto
print(f"Valor para cada colega após o desconto: R${valor}")


#Variável criada para passar pro próximo código
print("")
enter = input(str("Pressione ENTER para acessar o segundo código: "))
while enter!= (""):
    enter = input(str("Pressione somente a tecla ENTER: "))
print("")


#Versão 2 / valor /= divisor
valor = 675.00
divisor = 5
desconto = 15.00

print (f"Valor inicial: R${valor}")
valor /= divisor
print(f"Valor para cada colega: R${valor}")
valor -= desconto
print(f"Valor para cada colega após o desconto: R${valor}")