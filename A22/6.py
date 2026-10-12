def somar(numero):
    if numero == 1:
        return 1
    return numero + somar(numero - 1)


print(somar(5))
