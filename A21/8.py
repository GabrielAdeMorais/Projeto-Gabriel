pilha = []
from time import sleep

pilha.extend(["1- Procurando Remo", "2- Alice no país da corrupção", "3- Grande príncipe", "4- Branca de Neve e os Sete Ladrões", "5- Sem porquinhos"])

while len(pilha) > 0:
    retirado = pilha.pop()
    print (f"Retirando: {retirado}")
    sleep (1.5)