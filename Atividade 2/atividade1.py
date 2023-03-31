# Abrindo o arquivo Notas dos Alunos.txt em modo de escrita
with open("Notas dos Alunos.txt", "w") as notaAlunos:
    while True:
        # Coletando informações do usuário
        aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
        if aluno == "fim":
            break
        nota1 = float(input("Digite a nota 1 do aluno: "))
        nota2 = float(input("Digite a nota 2 do aluno: "))
        nota3 = float(input("Digite a nota 3 do aluno: "))
        
        # Salvando as informações no arquivo notas.txt
        notaAlunos.write(f"Nome: {aluno}\n Nota 1: {nota1} \n Nota 2: {nota2}\n Nota 3: {nota3}\n \n \n")

notaAlunos.close()
