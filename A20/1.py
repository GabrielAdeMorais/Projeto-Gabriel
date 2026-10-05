#LISTA
equipamentos = []


for i in range (3):
   

    print("")
    codigo = int(input(f"Digite o código do {i+1}° equipamento: ")) 
    nome = str(input("Digite o nome do equipamento: "))
    tipo = str(input("Digite o tipo do equipamento: "))
    quantidade = int(input("Digite a quantidade do equipamento: "))
    situacao= str(input("Digite a situação do equipamento: "))

    #DICIONÁRIO
    equipamento = {"código": codigo, "nome": nome, "tipo": tipo, "quantidade": quantidade, "situação": situacao}

    #FUNÇÃO APPEND
    equipamentos.append(equipamento)

#ESTRUTURA DE REPETIÇÃO PARA MOSTRAR AS INFORMAÇÕES PARA O USUÁRIO
for equipamento in equipamentos:
    print (equipamento)











 