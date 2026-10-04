equipamentos = []

contador = 0

for i in range(3):
    contador = contador + 1
    codigo = int(input(f"Digite o código do {contador}° equipamento: "))
    nome = input("Digite o nome do equipamento: ")
    tipo = input("Digite o tipo do equipamento: ")
    quantidade = int(input("Digite a quantidade: "))
    situacao = input("Digite a situação do equipamento: ")

    equipamento = {
        "codigo": codigo,
        "nome": nome,
        "tipo": tipo,
        "quantidade": quantidade,
        "situacao": situacao
    }

    equipamentos.append(equipamento)

print("\nEquipamentos cadastrados:")

for equipamento in equipamentos:
    print(equipamento)