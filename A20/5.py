estacionamento = []

for i in range(3):
    fileira = []

    for j in range(5):
        vaga = int(input(f"Digite a situação da vaga {j + 1} da fileira {i + 1} (0 = livre, 1 = ocupada): "))
        fileira.append(vaga)

    estacionamento.append(fileira)

print("\nESTACIONAMENTO:")

for fileira in estacionamento:
    print(fileira)

ocupadas = 0
livres = 0

for fileira in estacionamento:
    for vaga in fileira:
        if vaga == 1:
            ocupadas = ocupadas + 1
        else:
            livres = livres + 1

print("\nTotal de vagas:", 15)
print("Vagas ocupadas:", ocupadas)
print("Vagas livres:", livres)