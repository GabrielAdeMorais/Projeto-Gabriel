def fibonacci(posicao):
    if posicao == 0:
        return 0
    if posicao == 1:
        return 1
    return fibonacci(posicao - 1) + fibonacci(posicao - 2)

numero = int(input("Digite um número: "))
print(fibonacci(numero))
