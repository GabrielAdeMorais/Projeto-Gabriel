from time import sleep
acoes = [
"Digitou o nome",
"Alterou o endereço",
"Adicionou um produto",
"Alterou o telefone",
"Excluiu um produto"
]

while len(acoes):
    desfazer= acoes.pop()
    print (f"Desfazendo: {desfazer}")
    sleep (1.8)

