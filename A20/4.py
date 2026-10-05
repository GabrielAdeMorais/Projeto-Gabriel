#LISTA
funcionarios = []

#ESTRUTURA DE REPETIÇÃO
for i in range(5):

    matricula = int(input(f"Digite a matrícula do {i+1}° funcionário: "))
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor: ")
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salário: "))

    #DICIONÁRIO
    funcionario = {
        "matricula": matricula,
        "nome": nome,
        "setor": setor,
        "cargo": cargo,
        "salario": salario
    }

    #FUNÇÃO APPEND
    funcionarios.append(funcionario)

print("\nFuncionários cadastrados:")

for funcionario in funcionarios:
    print("Matrícula:", funcionario["matricula"])
    print("Nome:", funcionario["nome"])
    print("Setor:", funcionario["setor"])
    print("Cargo:", funcionario["cargo"])
    print("Salário:", funcionario["salario"])
    print()

matricula_busca = int(input("Digite a matrícula do funcionário que deseja procurar: "))

#VARIÁVEL CRIADA PARA VERIFICAR UMA CONDIÇÃO
encontrado = False

for funcionario in funcionarios:
    if funcionario["matricula"] == matricula_busca:
        print("\nFuncionário encontrado.")
        print("Matrícula:", funcionario["matricula"])
        print("Nome:", funcionario["nome"])
        print("Setor:", funcionario["setor"])
        print("Cargo:", funcionario["cargo"])
        print("Salário:", funcionario["salario"])
        encontrado = True

if encontrado == False:
    print("\nFuncionário não encontrado.")