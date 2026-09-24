#Mensagem de boas vindas ao usuário
print ("Bem vindo a Escola Virtual Senao")

#Coleta de dados do usuário
aluno = str (input("Digite o nome do aluno: "))

nota1 = 0
nota2 = 0
nota3 = 0

#Estrutura de repetição para verificar se o número é maior que 10 ou menor que 0
while (nota1 < 1 or nota1 >10) or (nota2 < 1 or nota2 >10) or (nota3 < 1 or nota3 > 10):
    print("Digite uma nota válida de 0 a 10: ")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    print ("")

media = (nota1+nota2+nota3)/3

freq = int (input("Digite a frenquência do aluno: "))

if freq < 75:
    situacao = "Reprovado por frequência!"
elif media >= 7:
    situacao = "Aprovado por nota!"
elif media >= 5:
    situacao = "O aluno está em recuperação!"
else:
    situacao = "O aluno está reprovado!"

#Resultado final
print("")
print("=" * 30)
print("       RESULTADO FINAL      ")
print("=" * 30)
print(f"Nome do estudante: {aluno}")
print(f"Média final:       {media:.2f}")
print(f"Frequência:        {freq}%")
print(f"Situação final:    {situacao}")


















