#Função
def calcular_media(nota1,nota2,nota3):
    return((nota1+nota2+nota3)/3)

#Solicitação das notas
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

#Calculo das notas
media = calcular_media(nota1, nota2, nota3)
print(f"A média é: {round(media,2)}")
