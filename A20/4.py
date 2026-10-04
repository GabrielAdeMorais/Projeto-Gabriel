funcionarios = []

contador = 0

for i in range(5):
    contador = contador + 1

    matricula = int(input(f"Digite a matrícula do {contador}° funcionário: "))
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor: ")
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salário: "))

    funcionario = {
        "matricula": matricula,
        "nome": nome,
        "setor": setor,
        "cargo": cargo,
        "salario": salario
    }

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