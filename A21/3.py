notas = []

for i in range(5):
    nota= float(input(f"Digite a nota do {i + 1}° aluno: "))
    
    while nota <0 or nota > 10:
        print("Digite uma nota válida de 0 a 10! ")
        nota= float(input(f"Digite a nota do {i + 1}° aluno: "))
              
    notas.append(nota)


print("Notas dos alunos: ")

for nota in notas:
    print(nota)

print ("Soma das notas:" , sum(notas))

media= sum(notas) / len(notas)
print(f"Média: {media}") 