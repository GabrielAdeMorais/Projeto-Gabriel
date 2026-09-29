#Função
def converter_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

#Solicitação da temperatura
celsius = int(input("Digite a temperatura em celsius: "))

#Resultado da temperatura convertida
print (f"A temperatura é: {converter_temperatura(celsius)} F°")