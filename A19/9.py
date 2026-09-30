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
    print (""===== MENU ====="")
    print ("1- Cadastrar usuário.")
    print ("2- Consultar usuário.")
    print ("3- Alterar usuário.")
    print ("4- Excluir usuário")
    print ("0- Sair")