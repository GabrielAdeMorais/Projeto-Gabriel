def mostrar_andares(andar):
    if andar == 0:
        return
    mostrar_andares(andar - 1)
    print("Andar", andar)


mostrar_andares(6)
