fila = []

from time import sleep

fila.extend(["Gabriel", "Marcel","Vitor","Andrei", "Artur"])

for pessoa in fila:
    print (f"Clientes aguardando: {pessoa}")

print("=============================")

for i in range(len(fila)):
    atendido = fila.pop(0)
    print (f"Atendendo: {atendido}")
    sleep (1.5)
    contador = len(fila)
    print (f"Clientes restantes: {contador}")
    print("")
    

print ("Fila vazia.")
print ("Todos os clientes foram atendidos!")