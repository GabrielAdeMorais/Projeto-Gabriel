#Solicitação de informação do usuário
nome = input("Digite o nome do cliente: ")
renda = float(input("Digite a renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor solicitado: R$ "))
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
divida = input("Possui alguma dívida em atraso? S ou N: ")

valor_parcela = valor_emprestimo / quantidade_parcelas

#If para verificar o empréstimo
if divida == "S":
    resultado = "Empréstimo negado"
    motivo = "Possui dívida em atraso"
elif valor_parcela > renda * 0.30:
    resultado = "Empréstimo negado"
    motivo = "A parcela ultrapassa 30% da renda"
elif valor_emprestimo > renda * 10:
    resultado = "Empréstimo negado"
    motivo = "O valor solicitado ultrapassa 10 vezes a renda"
elif quantidade_parcelas < 1 or quantidade_parcelas > 48:
    resultado = "Empréstimo negado"
    motivo = "A quantidade de parcelas deve estar entre 1 e 48"
else:
    resultado = "Empréstimo aprovado"
    motivo = "Nenhum"

#Resumo do empréstimo
print("")
print("--- RESUMO DO EMPRÉSTIMO ---")
print("Nome:", nome)
print("Valor solicitado:", valor_emprestimo)
print("Quantidade de parcelas:", quantidade_parcelas)
print("Valor de cada parcela:", valor_parcela)
print("Resultado:", resultado)
print("Motivo:", motivo)