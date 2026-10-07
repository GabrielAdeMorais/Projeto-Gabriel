from time import sleep

documentos = []

documentos.extend(["Relatório", "Contrato", "Currículo", "Nota fiscal", "Planilha" ])
print(f"Fila de impressão inicial: {documentos}")

for i in range (len(documentos)):
    imprimido = documentos.pop(0)
    sleep(1)
    print(f"Documento sendo impresso: {imprimido}")
    sleep(3)
    print ("Impressão concluída!")
    print ("")


print ("Todos documentos foram impressos.")
