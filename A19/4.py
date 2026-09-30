contador = 0
nomesLista = []

for nomes in range (1,6):
    contador = contador + 1
    nome= input(f"Digite o nome do {contador}° participante: ")
    nomesLista.append(nome)

print (f"Os nomes dos participantes são: {nomesLista}")