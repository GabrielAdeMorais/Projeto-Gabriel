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
elif pagamento == 2:
    desconto = (subtotal*8)/100
    valorFinal = subtotal - desconto
elif pagamento == 3:
    desconto = (subtotal*5)/100
    valorFinal = subtotal - desconto
else:
    valorFinal = subtotal
    print ("Informe a quantidade de parcelas: ")

 








