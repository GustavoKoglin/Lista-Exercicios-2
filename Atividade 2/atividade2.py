# Abrir arquivo notas.txt em modo de leitura
with open('Notas dos Alunos.txt', 'r') as notas:
    # Abrir arquivos de saída em modo de escrita
    with open('aprovados.txt', 'w') as aprovados, \
         open('exame.txt', 'w') as exame, \
         open('reprovados.txt', 'w') as reprovados:
             
        # Iterar sobre cada linha do arquivo notas.txt
        for linha in notas:
            # Dividir a linha em nome e notas (por vírgula)
            nome, nota1, nota2, nota3 = linha.strip().split('\n')
            # Converter as notas para float
            nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)
            # Calcular a média das notas
            media = (nota1 + nota2 + nota3) / 3
            print(linha)
            # Verificar o resultado do aluno
            if media >= 7:
                # Salvar informações do aluno em aprovados.txt
                aprovados.write(f'{nome}, {media:.2f}, Aprovado\n')
                aprovados.close()
            elif media >= 5:
                # Salvar informações do aluno em exame.txt
                exame.write(f'{nome}, {media:.2f}, Exame\n')
                exame.close()
            else:
                # Salvar informações do aluno em reprovados.txt
                reprovados.write(f'{nome}, {media:.2f}, Reprovado\n')
                reprovados.close()
notas.close()