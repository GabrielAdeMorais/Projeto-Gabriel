def somar(n1,n2):
    return n1+n2

def subtrair(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("")
print("Escolha uma das opções abaixo: ")
print("1- Somar.")
print("2- Subtrair.")
print("3- Multiplicar")
print("4- Dividir.")

print("")
opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    resultado = somar(n1,n2)
elif opcao == 2:
    resultado = subtrair(n1,n2)
elif opcao == 3:
    resultado = multiplicar(n1,n2)
else:
    resultado = dividir(n1,n2)

print("")
print("=" * 30)
print("RESULTADO".center(30))
print("=" * 30)
print(f"O resultado é: {resultado}")