item = str (input("Digite o produto armazenado: "))
quantidade = int(input("Digite a quantidade em estoque desse produto: "))

while quantidade <= 0:
    print ("O número não pode ser menor que 1, digite uma quantidade válida!")
    print ("")
    quantidade = int(input("Digite a quantidade em estoque desse produto: "))

print(f"Há {quantidade} unidade(s) do produto {item}.")


