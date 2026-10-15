#Versão 1 / saldo = saldo - valor
saldo = 500.00

print(f"Valor inicial: R${saldo} ")

valor = 125.00
saldo = saldo - valor

print(f"Valor após a primeira compra: R${saldo}")

valor = 89.00

saldo = saldo - valor
print(f"Valor após a segunda compra: R${saldo}")

if saldo > 200:
    print ("Você ainda tem saldo para realizar uma nova compra de R$200,00")
else:
    print ("Você não possui saldo suficiente para uma nova compra de R$200,00")


#Variável criada para passar pro próximo código
print("")
enter = input(str("Pressione ENTER para acessar o segundo código: "))
while enter!= (""):
    enter = input(str("Pressione somente a tecla ENTER: "))
print("")


#Versão 2 / saldo -= valor
saldo = 500.00

print(f"Valor inicial: R${saldo} ")

valor = 125.00
saldo -= valor

print(f"Valor após a primeira compra: R${saldo}")

valor = 89.00

saldo -= valor
print(f"Valor após a segunda compra: R${saldo}")

if saldo > 200:
    print ("Você ainda tem saldo para realizar uma nova compra de R$200,00")
else:
    print ("Você não possui saldo suficiente para uma nova compra de R$200,00")