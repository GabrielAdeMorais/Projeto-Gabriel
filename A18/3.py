#Função
def maior_numero(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2


#Solicitação de número
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

#Resultado do maior número
print(f"O maior número é: {maior_numero(n1,n2)}")   
    

