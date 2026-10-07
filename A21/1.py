alunos = []

for i in range (5):
    aluno= input(f"Digite o nome do {i + 1}° aluno: ")
    alunos.append(aluno)


print("Alunos cadastrados:")
for aluno in alunos:
    print(aluno)

print()

print("Primeiro aluno:", alunos[0])
print("Último aluno:", alunos[-1])

print()

aluno = input("Digite o nome do novo aluno: ")
alunos.append(aluno)

print()
print("Lista atualizada:")
for aluno in alunos:
    print(aluno)