pedidos = []

contador = 0

for i in range(5):
    contador = contador + 1

    numero = int(input(f"Digite o número do {contador}° pedido: "))
    cliente = input("Digite o nome do cliente: ")
    produto = input("Digite o produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    situacao = input("Digite a situação do pedido: ")

    pedido = {
        "numero": numero,
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "situacao": situacao
    }

    pedidos.append(pedido)

print("\nPEDIDOS CADASTRADOS:")

for pedido in pedidos:
    valor_total = pedido["quantidade"] * pedido["valor_unitario"]

    print("Número:", pedido["numero"])
    print("Cliente:", pedido["cliente"])
    print("Produto:", pedido["produto"])
    print("Quantidade:", pedido["quantidade"])
    print("Valor unitário:", pedido["valor_unitario"])
    print("Valor total:", valor_total)
    print("Situação:", pedido["situacao"])
    print()

numero_busca = int(input("Digite o número do pedido que deseja procurar: "))

encontrado = False

for pedido in pedidos:
    if pedido["numero"] == numero_busca:
        valor_total = pedido["quantidade"] * pedido["valor_unitario"]

        print("\nPedido encontrado.")
        print("Número:", pedido["numero"])
        print("Cliente:", pedido["cliente"])
        print("Produto:", pedido["produto"])
        print("Quantidade:", pedido["quantidade"])
        print("Valor unitário:", pedido["valor_unitario"])
        print("Valor total:", valor_total)
        print("Situação:", pedido["situacao"])

        encontrado = True

if encontrado == False:
    print("\nPedido não encontrado.")