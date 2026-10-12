def contar_alunos(quantidade):
    if quantidade == 0:
        return
    contar_alunos(quantidade - 1)
    print("Aluno", quantidade)

print("Contagem de aluno iniciando!")
contar_alunos(5)
