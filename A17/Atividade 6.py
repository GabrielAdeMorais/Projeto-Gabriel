nome = input("Digite o nome do participante: ")
idade = int(input("Digite a idade: "))
quantidade = int(input("Digite a quantidade de ingressos: "))

print("1 - Estudante")
print("2 - Professor")
print("3 - Público geral")
categoria = int(input("Digite a categoria: "))

if categoria == 1:
    valor_ingresso = 20
    nome_categoria = "Estudante"
elif categoria == 2:
    valor_ingresso = 25
    nome_categoria = "Professor"
else:
    valor_ingresso = 40
    nome_categoria = "Público geral"

valor_original = valor_ingresso * quantidade

if idade < 10:
    desconto = valor_original
    valor_final = 0
elif idade >= 60:
    desconto = valor_original * 0.50
    valor_final = valor_original - desconto
elif quantidade >= 5:
    desconto = valor_original * 0.10
    valor_final = valor_original - desconto
else:
    desconto = 0
    valor_final = valor_original

print("")
print("--- RESUMO DA COMPRA ---")
print("Nome:", nome)
print("Categoria:", nome_categoria)
print("Valor original:", valor_original)
print("Desconto:", desconto)
print("Valor final:", valor_final)