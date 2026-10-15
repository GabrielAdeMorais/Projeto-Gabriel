#Versão 1 / vagas = vagas - 1
vagas = 15

for i in range (4):
    vagas = vagas - 1

if vagas == 0:
    print ("Não há vagas disponíveis!")
else:
    print (f"Há {vagas} vagas disponíveis!")


#Variável criada para passar pro próximo código
print("")
enter = input(str("Pressione ENTER para acessar o segundo código: "))
while enter!= (""):
    enter = input(str("Pressione somente a tecla ENTER: "))
print("")


#Versão 2 / vagas -=
vagas = 15

for i in range (4):
    vagas -= 1

if vagas == 0:
    print ("Não há vagas disponíveis!")
else:
    print (f"Há {vagas} vagas disponíveis!")