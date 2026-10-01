nomes = []
notas = []
ap = 0
rec = 0
rep= 0
for i in range(5):
    nome = str(input("Digite o nome do estudante: "))
    nota = float(input(f"Digite a nota do {nome}: "))
    while nota > 10 or nota < 0:
        nota = float(input("Ocorreu um erro! Digite uma nota de 1 a 10: "))
    nomes.append(nome)
    notas.append(nota)

    if notas[i] >= 7:
        print(f"O aluno {nomes[i]} foi aprovado!")
        ap += 1

    elif notas[i] >=5:
        print(f"O aluno {nomes[i]} está em recuperação!")
        rec += 1
    else:
        print(f"O aluno {nomes[i]} está reprovado!")
        rep += 1

print("")
print(f"Existem {ap} alunos aprovados!")
print(f"Existem {rec} alunos em recuperação!")
print(f"Existem {rep} alunos reprovados!")






