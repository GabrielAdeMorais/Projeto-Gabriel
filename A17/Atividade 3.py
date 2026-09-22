nome = str (input("Digite seu nome: "))
produto = str (input("Informe seu produto: "))
preco_unitario = float(input("Informe o preço unitário do produto: "))
quantidade = int (input("Informe a quantidade comprada: "))

subtotal = preco_unitario*quantidade

print ("")
print ("Qual será a forma de pagamento?")
print ("1- PIX")
print ("2- Dinheiro")
print ("3- Cartão de débito")
print ("4- Cartão de crédito")
pagamento = int (input("Escolha uma das opções: "))

while pagamento <=0 or pagamento >4:
    pagamento = int(input("Selecione uma opção válida: "))

if pagamento == 1:
    desconto = (subtotal*10)/100
    valorFinal = subtotal - desconto
    forma = "PIX"
elif pagamento == 2:
    desconto = (subtotal*8)/100
    valorFinal = subtotal - desconto
    forma = "Dinheiro"
elif pagamento == 3:
    desconto = (subtotal*5)/100
    valorFinal = subtotal - desconto
    forma = "Cartão de débito"
else:
    desconto = 0
    forma = "Cartão de crédito"
    
    parcela = int(input("Informe a quantidade de parcelas: "))

    while parcela <= 0 or parcela > 12:
        parcela = int(input("Selecione uma quantidade de parcelas válida: "))

    if parcela <= 3:
        juros = 0
    else:
        juros = (subtotal * 6) / 100

    valorFinal = subtotal + juros

print("")
print("========== COMPROVANTE ==========")
print("Cliente:", nome)
print("Produto:", produto)
print("Subtotal: R$", subtotal)

if pagamento == 4:
    print("Acréscimo: R$", juros)
else:
    print("Desconto: R$", desconto)

print("Valor final: R$", valorFinal)
print("Forma de pagamento:", forma)

 








