#LISTA
veiculos = []

#ESTRUTURA DE REPETIÇÃO
for i in range(4):

    codigo = int(input(f"Digite o código do {i+1}° veículo: "))
    placa = input("Digite a placa: ")
    modelo = input("Digite o modelo: ")
    marca = input("Digite a marca: ")
    ano = int(input("Digite o ano: "))
    quilometragem = int(input("Digite a quilometragem: "))
    situacao = input("Digite a situação: ")

    #DICIONÁRIO
    veiculo = {
        "codigo": codigo,
        "placa": placa,
        "modelo": modelo,
        "marca": marca,
        "ano": ano,
        "quilometragem": quilometragem,
        "situacao": situacao
    }

    veiculos.append(veiculo)

print("\nVEÍCULOS CADASTRADOS:")

for veiculo in veiculos:
    print("Código:", veiculo["codigo"])
    print("Placa:", veiculo["placa"])
    print("Modelo:", veiculo["modelo"])
    print("Marca:", veiculo["marca"])
    print("Ano:", veiculo["ano"])
    print("Quilometragem:", veiculo["quilometragem"])
    print("Situação:", veiculo["situacao"])
    print()

placa_busca = input("Digite a placa do veículo que deseja procurar: ")

#VARIÁVEL CRIADA PARA VERIFICAR UMA CONDIÇÃO
encontrado = False

#FOR JUNTO COM PRINT E IF USADO PARA MOSTRAR AS INFORMAÇÕES PARA O USUÁRIO
for veiculo in veiculos:
    if veiculo["placa"] == placa_busca:
        print("\nVeículo encontrado.")
        print("Código:", veiculo["codigo"])
        print("Placa:", veiculo["placa"])
        print("Modelo:", veiculo["modelo"])
        print("Marca:", veiculo["marca"])
        print("Ano:", veiculo["ano"])
        print("Quilometragem:", veiculo["quilometragem"])
        print("Situação:", veiculo["situacao"])
        encontrado = True

if encontrado == False:
    print("\nVeículo não encontrado.")

maior_quilometragem = veiculos[0]

for veiculo in veiculos:
    if veiculo["quilometragem"] > maior_quilometragem["quilometragem"]:
        maior_quilometragem = veiculo

print("\nVEÍCULO COM MAIOR QUILOMETRAGEM:")
print("Placa:", maior_quilometragem["placa"])
print("Modelo:", maior_quilometragem["modelo"])
print("Quilometragem:", maior_quilometragem["quilometragem"])