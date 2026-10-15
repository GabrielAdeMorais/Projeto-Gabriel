#Versão 1 / total = total * fator
total = 35
fator = 4

print(f"Valor inicial de etiquetas: {total}")
total = total * fator
print(f"Valor total de etiquetas após impressão em 4 lotes: {total}")
fator = 2
total = total * fator
print(f"Valor total de etiquetas após outra solicitação equivalente: {total}")


#Variável criada para passar pro próximo código
print("")
enter = input(str("Pressione ENTER para acessar o segundo código: "))
while enter!= (""):
    enter = input(str("Pressione somente a tecla ENTER: "))
print("")


#Versão 2 / total *= fator
total = 35
fator = 4

print(f"Valor inicial de etiquetas: {total}")
total *= fator
print(f"Valor total de etiquetas após impressão em 4 lotes: {total}")
fator = 2
total *= fator
print(f"Valor total de etiquetas após outra solicitação equivalente: {total}")
