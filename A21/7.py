pedidos = []
from time import sleep

for i in range (5):
    pedido = input(f"Digite o {i+1}° produto: ")
    pedidos.append(pedido)

print("\nPedidos aguardando: ")

for pedido in pedidos:
    sleep (1)
    print (pedido)

print ("===============================")

while len(pedidos) > 0:
    proc= pedidos.pop(0)
    sleep (2)
    print (f"Pedidos em processamento: {proc}")

sleep (1)
print ("================================")
print ("Todos pedidos foram processados!")





    