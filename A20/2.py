estoque = []

contador = 0

for i in range(5):
    contador = contador + 1

    codigo = int(input(f"Digite o código do {contador}° produto: "))
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    quantidade = int(input("Digite a quantidade atual: "))
    quantidade_minima = int(input("Digite a quantidade mínima: "))
    preco = float(input("Digite o preço do produto: "))

    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "quantidade_minima": quantidade_minima,
        "preco": preco
    }

    estoque.append(produto)

print("\nProdutos cadastrados:")

for produto in estoque:
    print("Código:", produto["codigo"])
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Quantidade atual:", produto["quantidade"])
    print("Quantidade mínima:", produto["quantidade_minima"])
    print("Preço:", produto["preco"])
    print()

print("PRODUTOS QUE NECESSITAM DE REPOSIÇÃO")

for produto in estoque:
    if produto["quantidade"] <= produto["quantidade_minima"]:
        print("Código:", produto["codigo"])
        print("Produto:", produto["nome"])
        print("Quantidade atual:", produto["quantidade"])
        print("Quantidade mínima:", produto["quantidade_minima"])
        print()