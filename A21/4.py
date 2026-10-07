nomes = []

for i in range (5):
    nome= input(f"Digite o nome da {i + 1}° pessoa: ")
    nomes.append(nome)

print ("Pessoas cadastradas:" )
print ("")
       
for nome in nomes:
    print (nome)