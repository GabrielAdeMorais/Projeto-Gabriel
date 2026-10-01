verificacao= False

usuario = str(input("Digite o nome do usuário: "))

for i in range (3):
       
    
    senha = str(input("Digite a senha: "))


    if senha == "jacarino":
        print("Acesso autorizado!")
        verificacao= True
        break
    else:
         print("Acesso negado! Digite a senha novamente: ")
    

if verificacao== False:
    print("Acesso bloqueado!")
