def contar_alunos(quantidade):
    if quantidade == 0:
        return
    contar_alunos(quantidade - 1)
    print("Aluno", quantidade)

numero_alunos = int(input("Digite a quantidade de alunos: "))
print("Contagem de aluno iniciando!")
contar_alunos(numero_alunos)
