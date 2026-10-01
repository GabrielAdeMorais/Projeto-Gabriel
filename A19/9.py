def cadastrar_usuario():
    nome = input("Digite o nome do cliente: ")
    print(f"Cliente {nome} cadastrado com sucesso!")


def consultar_usuario():
    nome = input("Digite o nome do cliente: ")
    print(f"Consultando cliente: {nome}")


def alterar_usuario():
    nome = input("Digite o nome do cliente: ")
    print (f"Alterando cliente: {nome}")


def excluir_usuario():
    nome = input("Digite o nome do cliente:")
    print(f"Excluindo cliente {nome}")


while True:
    print ("===== MENU =====")
    print ("1- Cadastrar usuário.")
    print ("2- Consultar usuário.")
    print ("3- Alterar usuário.")
    print ("4- Excluir usuário")
    print ("0- Sair")

    opcao = (input("Escolha uma opção:")) 

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        consultar_usuario()

    elif opcao == "3":
        alterar_usuario()

    elif opcao == "4":
        excluir_usuario()

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
