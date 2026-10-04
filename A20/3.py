livros = []

contador = 0

for i in range(4):
    contador = contador + 1

    codigo = int(input(f"Digite o código do {contador}° livro: "))
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de publicação: "))
    quantidade = int(input("Digite a quantidade disponível: "))

    livro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "quantidade": quantidade
    }

    livros.append(livro)

print("\nLivros cadastrados:")

for livro in livros:
    print("Código:", livro["codigo"])
    print("Título:", livro["titulo"])
    print("Autor:", livro["autor"])
    print("Ano:", livro["ano"])
    print("Quantidade disponível:", livro["quantidade"])
    print()

codigo_busca = int(input("Digite o código do livro que deseja procurar: "))

encontrado = False

for livro in livros:
    if livro["codigo"] == codigo_busca:
        print("\nLivro encontrado.")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Quantidade disponível:", livro["quantidade"])
        encontrado = True

if encontrado == False:
    print("\nLivro não encontrado.")