import random
senha_Correta = random.randint (1,20)
senha = int(input("Digite a senha correta: "))
print("Dica: um número de 1 a 20")

while senha != senha_Correta:
    print ("Senha incorreta, tente novamente!")
    senha= int(input("Digite novamente: "))

print ("Você acertou!")