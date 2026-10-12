def contagem_regressiva(numero):
    if numero == 0:
        return
    print(numero)
    contagem_regressiva(numero - 1)

numero_usuario = int(input("Digite um número: "))

print("Contagem regressiva iniciando!")
contagem_regressiva(numero_usuario)
