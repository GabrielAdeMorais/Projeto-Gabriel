produtos= []

for i in range(5):
    produto= input(f"Digite o {i + 1}° produto: ")
    produtos.append(produto)

for produto in produtos:
    print (produto)