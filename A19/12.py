def cadastrar_aluno():
    global nome, alunos

    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

    print(f"Aluno {nome} cadastrado com sucesso!")


def consultar_alunos(alunos):
    global nome, verificador

    nome = input("Digite o nome do aluno: ")
    verificador = False

    print(f"Consultando aluno: {nome}")

    for i in range(len(alunos)):
        if alunos[i] == nome:
            verificador = True

    if verificador == True:
        print("Aluno encontrado!")
    else:
        print("Aluno não encontrado!")


def registrar_nota():
    global nome, notas

    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    notas[nome] = nota

    print(f"Nota {nota} registrada para o aluno {nome}!")


def quantidade_alunos():
    global alunos

    print(f"Quantidade de alunos: {len(alunos)}")


# PYTHON GLOBAL

nome = ""
alunos = []
verificador = False
notas = {}


while True:
    print("")
    print("-----------------------------")
    print("      SISTEMA ESCOLA")
    print("-----------------------------")
    print("")
    print("1 - Cadastrar aluno")
    print("2 - Consultar alunos")
    print("3 - Registrar nota")
    print("4 - Exibir quantidade de alunos")
    print("0 - Encerrar sistema")
    print("")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Opção 1 selecionada.")
        cadastrar_aluno()

    elif opcao == "2":
        print("Opção 2 selecionada.")
        consultar_alunos(alunos)

    elif opcao == "3":
        print("Opção 3 selecionada.")
        registrar_nota()

    elif opcao == "4":
        print("Opção 4 selecionada.")
        quantidade_alunos()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")