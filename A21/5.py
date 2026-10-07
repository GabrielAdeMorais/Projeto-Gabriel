fila= []

fila.extend(["Luffy", "Zoro", "Sanji", "Nami", "Robin"])
print(f"Fila: {fila}")

for i in range (5):
    atendido = fila.pop(0)

    print ("")
    print (f"Pessoa atendida: {atendido}")
    print ("")
    if len(fila) == 0:
        print("Fim do atendimento. Todas pessoas foram atendidas!")
        break
    else:
        print (f"Fila após atendimento: {fila}")

    
