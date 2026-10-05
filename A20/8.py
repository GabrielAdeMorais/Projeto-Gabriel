#LISTA
temperaturas = []

#ESTRUTURA DE REPETIÇÃO
for i in range(3):
    ambiente = []

    for j in range(4):
        temperatura = float(input(f"Digite a temperatura do sensor {j + 1} do ambiente {i + 1}: "))
        ambiente.append(temperatura)

    temperaturas.append(ambiente)

print("\nTEMPERATURAS:")

for ambiente in temperaturas:
    print(ambiente)

print("\nMÉDIA DE CADA AMBIENTE:")

for i in range(3):
    soma = 0

    for temperatura in temperaturas[i]:
        soma = soma + temperatura

    media = soma / 4

    print("Ambiente", i + 1, ":", media)

maior = temperaturas[0][0]
menor = temperaturas[0][0]

for ambiente in temperaturas:
    for temperatura in ambiente:
        if temperatura > maior:
            maior = temperatura

        if temperatura < menor:
            menor = temperatura

print("\nMaior temperatura registrada:", maior)
print("Menor temperatura registrada:", menor)