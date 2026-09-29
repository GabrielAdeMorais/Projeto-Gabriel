#Função
def verificar_situacao(media):
    if (media>=7):
        return "Aprovado"
    elif (media>=5 and media<=6.9):
        return "Recuperação"
    else:
        return "Reprovado"

#Solicitação da média e resultado
media = float(input("Digite sua média: "))
print(verificar_situacao(media))
