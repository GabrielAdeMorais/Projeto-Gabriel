#Versão 1 / contador = contador + 1
contador = 0
from time import sleep

for i in range (3):
    contador = contador + 1
    print (f"Acesso {contador}")
    sleep (1)

print("")
print(f"Quantidade total de acesso: {contador}")


#Variável criada para passar pro próximo código
print("")
enter = input(str("Pressione ENTER para acessar o segundo código: "))
while enter!= (""):
    enter = input(str("Pressione somente a tecla ENTER: "))
print("")


#Versão 2 / +=
contador = 0

for i in range (3):
    contador+=1
    print (f"Acesso {contador}")
    sleep (1)

print("")
print(f"Quantidade total de acesso: {contador}")