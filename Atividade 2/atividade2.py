with open("notas.txt", "r") as arquivo:
    # Loop para ler cada linha do arquivo
    for linha in arquivo:
        # Divide a linha em uma lista de strings separadas por vírgulas
        dados = linha.strip().split(",")
        # Extrai as informações do aluno
        nome = dados[0]
        nota1 = float(dados[1])
        nota2 = float(dados[2])
        nota3 = float(dados[3])
        # Calcula a média das notas
        media = (nota1 + nota2 + nota3) / 3
        # Verifica a situação do aluno
        if media >= 7:
            situacao = "Aprovado"
            arquivo_saida = "aprovados.txt"
        elif media >= 5:
            situacao = "Exame"
            arquivo_saida = "exame.txt"
        elif media < 5:
            situacao = "Reprovado"
            arquivo_saida = "reprovados.txt"
        # Salva as informações do aluno no arquivo correspondente
        with open(arquivo_saida, "a") as saida:
            saida.write(f"{nome} - Media: {media:.2f} - Situacao: {situacao}\n")