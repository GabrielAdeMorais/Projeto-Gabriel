def descer_elevador(andar):
    if andar == 0:
        print(andar)
        print("Térreo")
        return
    print(andar)
    descer_elevador(andar - 1)

andares = int(input("Digite a quantidade de andares: "))
descer_elevador(andares)
