def converter_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = int(input("Digite a temperatura em celsius: "))

print (f"A temperatura é: {converter_temperatura(celsius)} F°")