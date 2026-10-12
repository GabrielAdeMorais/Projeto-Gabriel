def potencia(base, expoente):
    if expoente == 0:
        return 1
    elif expoente < 0:
        return 1 / potencia(base, expoente * -1)
    else:
        resultado = base * potencia(base, expoente - 1)
        return resultado


print(potencia(2, 3))
print(potencia(5, 2))
print(potencia(3, 3))
print(potencia(10, 2))
