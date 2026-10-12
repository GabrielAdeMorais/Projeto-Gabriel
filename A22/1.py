def contagem_regressiva(numero):
    if numero == 0:
        return
    print(numero)
    contagem_regressiva(numero - 1)

print("Contagem regressiva iniciando!")
contagem_regressiva(5)
