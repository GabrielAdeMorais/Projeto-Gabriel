#LISTA
producao = []

#ESTRUTURA DE REPETIÇÃO
for i in range(3):
    maquina = []

    for j in range(5):
        quantidade = int(input(f"Digite a produção da máquina {i + 1} no dia {j + 1}: "))
        maquina.append(quantidade)

    producao.append(maquina)

print("\n===== PRODUÇÃO SEMANAL =====")

totais = []

for i in range(3):
    total = 0

    for quantidade in producao[i]:
        total = total + quantidade

    #FUNÇÃO APPEND
    totais.append(total)

    print("Máquina", i + 1, ":", total, "unidades")

total_industria = 0

for total in totais:
    total_industria = total_industria + total

print("\nTotal produzido pela indústria:", total_industria, "unidades")

maior = totais[0]
maquina_maior = 1

for i in range(1, 3):
    if totais[i] > maior:
        maior = totais[i]
        maquina_maior = i + 1

print("Máquina que mais produziu:", maquina_maior)
print("Quantidade produzida:", maior, "unidades")