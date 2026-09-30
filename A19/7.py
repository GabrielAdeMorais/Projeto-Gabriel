print("Digite os números que deseja somar! ")
print("OBS: Digite 0 para encerrar e somar os números digitados.")

resultado = 0
numeros = 1

while numeros > 0:
    
    numeros = int(input("Digite os números que deseja somar: "))
    resultado = resultado + numeros

print (f"O resultado da soma dos números é: {resultado}")

