idade = 0

while True:
    print ("")
    idade = int(input("Digite sua idade:"))
    if idade < 18:
        print("Idade inválida, tente novamente.")
    
    elif idade >= 18:
        print("Seja bem-vindo(a!")
        break
