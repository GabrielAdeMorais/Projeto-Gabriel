#Versão 1 / orcamento = orcamento + valor
orcamento = 2500.00
valor1 = 750.00
valor2 = 300.00

print (f"Orçamento inicial: R${orcamento}")

orcamento = orcamento + valor1
print(f"Orçamento depois do primeiro acréscimo: R${orcamento} ")
orcamento = orcamento + valor2
print(f"Orçamento depois do segundo acréscimo: R${orcamento} ")

#Variável criada para passar pro próximo código
print("")
enter = input(str("Pressione ENTER para acessar o segundo código: "))
while enter!= (""):
    enter = input(str("Pressione somente a tecla ENTER: "))
print("")

#Versão 2 / orcamento += valor
orcamento = 2500.00
valor1 = 750.00
valor2 = 300.00

print (f"Orçamento inicial: R${orcamento}")

orcamento += valor1
print(f"Orçamento depois do primeiro acréscimo: R${orcamento} ")
orcamento += valor2
print(f"Orçamento depois do segundo acréscimo: R${orcamento} ")   
