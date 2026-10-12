def mostrar_mensagem(mensagem, quantidade):
    if quantidade == 0:
        return
    print(mensagem)
    mostrar_mensagem(mensagem, quantidade - 1)


mostrar_mensagem("Atenção!", 3)
