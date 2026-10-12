def somar(numero):
    if numero == 1:
        return 1
    return numero + somar(numero - 1)

numero_usuario = int(input("Digite um número para soma-ló em sequência: "))
print(somar(numero_usuario))
