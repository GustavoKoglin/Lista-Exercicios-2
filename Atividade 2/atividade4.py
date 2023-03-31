# Abrir o arquivo aprovados.txt em modo de leitura
with open('aprovados.txt', 'r') as arquivo_aprovados:
    # Iterar pelas linhas do arquivo
    for linha in arquivo_aprovados:
        # Dividir a linha em colunas
        colunas = linha.split()
        # Imprimir o nome do aluno e a legenda
        print(colunas[0], colunas[1], "Aprovado após exame")

# Abrir o arquivo reprovados.txt em modo de leitura
with open('reprovados.txt', 'r') as arquivo_reprovados:
    # Iterar pelas linhas do arquivo
    for linha in arquivo_reprovados:
        # Dividir a linha em colunas
        colunas = linha.split()
        # Imprimir o nome do aluno e a legenda
        print(colunas[0], colunas[1], "Reprovado após exame")