def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    return numero * fatorial(numero - 1)

numero_Usuario = int(input("Digite um número: "))
print(fatorial(numero_Usuario))
