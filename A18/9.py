#Funções
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    print(f"Cliente {nome} cadastrado com sucesso!")


def consultar_cliente():
    nome = input("Digite o nome do cliente: ")
    print(f"Consultando cliente: {nome}")


def calcular_compra():
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    total = preco * quantidade

    print(f"Valor total da compra: R$ {total:.2f}")


#Estrutura de repetição
while True:
    print("")
    print("\n--- MENU ---")
    print("1 - Cadastrar cliente")
    print("2 - Consultar cliente")
    print("3 - Calcular compra")
    print("4 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        consultar_cliente()
    elif opcao == 3:
        calcular_compra()
    elif opcao == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")