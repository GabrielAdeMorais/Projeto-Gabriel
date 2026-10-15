#Versão 1 / quantidade // divisor
quantidade = 53
divisor = 4
total = quantidade

print(f"Quantidade inicial: {quantidade}")
kits = quantidade // divisor
print(f"Podem ser montados {kits} completos.")
sobras = quantidade % divisor
print(f"Sobrará {sobras} matérial(s).")

confirmador = kits * divisor + sobras

if confirmador == total:
    print ("A soma dos materiais utilizando os kits com a sobra corresponde ao total recebido.")
else:
    print ("A soma dos materiais utilizando os kits com a sobra não corresponde ao total recebido.")


#Variável criada para passar pro próximo código
print("")
enter = input(str("Pressione ENTER para acessar o segundo código: "))
while enter!= (""):
    enter = input(str("Pressione somente a tecla ENTER: "))
print("")


# Versão 2 / quantidade //= divisor
quantidade = 53
divisor = 4
total = quantidade

print(f"Quantidade inicial: {quantidade}")

sobras = quantidade % divisor
quantidade //= divisor
kits = quantidade

print(f"Podem ser montados {kits} kits completos.")
print(f"Sobrará {sobras} material(is).")

confirmador = kits * divisor + sobras

if confirmador == total:
    print("A soma dos materiais dos kits com as sobras corresponde ao total recebido.")
else:
    print("A soma dos materiais dos kits com as sobras não corresponde ao total recebido.")