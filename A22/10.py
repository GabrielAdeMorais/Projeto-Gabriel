def processar(etapas):
    if etapas == 0:
        print("Processamento concluído!")
        return
    print("Processando...")
    processar(etapas - 1)


processar(3)
