while True:
    # Pede o nome do aluno e as notas
    aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    if aluno == "fim":
        break
    nota1 = float(input("Digite a nota 1 do aluno: "))
    nota2 = float(input("Digite a nota 2 do aluno: "))
    nota3 = float(input("Digite a nota 3 do aluno: "))

    # Salva as informações em um arquivo
    with open("notas.txt", "a") as arquivo:
        arquivo.write(f"{aluno},{nota1},{nota2},{nota3}\n")
arquivo.close()