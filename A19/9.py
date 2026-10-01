def cadastrar_usuario():
    global nome, usuarios
    nome = input("Digite o nome do cliente: ")
    print(f"Cliente {nome} cadastrado com sucesso!")
    usuarios.append(nome)


def consultar_usuario(usuarios):
    global nome, verificador
    verificador= False
    nome = input("Digite o nome do cliente: ")
    print(f"Consultando cliente: {nome}")
    for i in range(len(usuarios)):
        if usuarios[i] == nome:
            verificador= True

    if verificador== True:
        print ("Usuário encontrado!")
    else:
        print("Usuário não encontrado!")


def alterar_usuario(usuarios):
    global novo_nome
    nome = input("Digite o nome do cliente que deseja alterar: ")

    encontrado = False

    for i in range(len(usuarios)):
        if usuarios[i] == nome:
            novo_nome = input("Digite o novo nome: ")
            encontrado = True
            usuarios[i] = novo_nome

    if encontrado == True:
        print("Usuário alterado com sucesso!")
    else:
        print("Usuário não encontrado!")                            



def excluir_usuario():
    global usuarios, nome
    nome = input("Digite o nome do cliente que deseja excluir: ")

    excluido = False

    for i in range (len(usuarios)):
     

         if usuarios[i] == nome:
            del usuarios[i]
            excluido = True        

    if excluido == True:
        print("Usuário excluido com sucesso!")
    else:
        print("Usuário não encontrado!")
            

# PYTHON GLOBAL

nome= ""
usuarios= []
verificador= False
novo_nome= ""           
    



while True:
    print ("")
    print ("===== MENU =====")
    print ("1- Cadastrar usuário.")
    print ("2- Consultar usuário.")
    print ("3- Alterar usuário.")
    print ("4- Excluir usuário")
    print ("0- Sair")

    opcao = (input("Escolha uma opção: ")) 

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        consultar_usuario(usuarios)

    elif opcao == "3":
        alterar_usuario(usuarios)

    elif opcao == "4":
        excluir_usuario()

    elif opcao == "0":
        print("Saindo do sistema...")
        print(usuarios)
        break

    else:
        print("Opção inválida!")
