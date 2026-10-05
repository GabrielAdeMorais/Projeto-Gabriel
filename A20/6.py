#LISTA
salas = []

#ESTRUTURA DE REPETIÇÃO
for i in range(3):
    sala = []

    for j in range(4):
        situacao = int(input(f"Digite a situação da sala {i + 1}, período {j + 1} (0 = disponível, 1 = ocupado): "))
        sala.append(situacao)

    salas.append(sala)

print("\nAGENDA DAS SALAS:")

for sala in salas:
    print(sala)

sala_busca = int(input("\nDigite o número da sala (1 a 3): "))
periodo_busca = int(input("Digite o período (1 a 4): "))

situacao = salas[sala_busca - 1][periodo_busca - 1]

if situacao == 0:
    print("O horário está disponível.")
else:
    print("O horário está ocupado.")

print("\nHorários disponíveis por sala:")

for i in range(3):
    disponiveis = 0

    for j in range(4):
        if salas[i][j] == 0:
            disponiveis = disponiveis + 1

    print("Sala", i + 1, ":", disponiveis, "horários disponíveis")