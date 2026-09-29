#Funções
def cadastrar_produto():
    produto = input("Produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    return produto, preco, quantidade


def calcular_subtotal(preco, quantidade):
    return preco * quantidade


def aplicar_desconto(subtotal):
    if subtotal >= 500:
        return subtotal * 0.10
    else:
        return 0


def calcular_pagamento(subtotal, desconto):
    return subtotal - desconto


def exibir_resumo(produto, subtotal, desconto, total):
    print("")
    print("\n--- RESUMO DA COMPRA ---")
    print(f"Produto: {produto}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total: R$ {total:.2f}")


produto = ""
preco = 0
quantidade = 0
subtotal = 0
desconto = 0
total = 0

#Estrutura de repetição com Se para verificar qual opção foi escolhida
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar produto")
    print("2 - Calcular subtotal")
    print("3 - Aplicar desconto")
    print("4 - Calcular pagamento")
    print("5 - Exibir resumo da compra")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        produto, preco, quantidade = cadastrar_produto()

    elif opcao == 2:
        subtotal = calcular_subtotal(preco, quantidade)
        print(f"Subtotal: R$ {subtotal:.2f}")

    elif opcao == 3:
        desconto = aplicar_desconto(subtotal)
        print(f"Desconto: R$ {desconto:.2f}")

    elif opcao == 4:
        total = calcular_pagamento(subtotal, desconto)
        print(f"Total: R$ {total:.2f}")

    elif opcao == 5:
        exibir_resumo(produto, subtotal, desconto, total)

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")