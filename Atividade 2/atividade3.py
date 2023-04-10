# Função para calcular a nova média
def calcular_media(nota1, nota2, nota3, nota_exame, media_anterior):
    nova_media = (nota1 + nota2 + nota3 + nota_exame) / 4.0
    if media_anterior is not None:
        nova_media = (nova_media + media_anterior) / 2.0
    return nova_media


# Ler o arquivo exame.txt
with open('exame.txt', 'r') as file:
    linhas = file.readlines()

# Atualizar os arquivos aprovados.txt e reprovados.txt
with open('aprovados.txt', 'a') as aprovados_file:
    with open('reprovados.txt', 'a') as reprovados_file:
        for linha in linhas:
            # Obter as informações do aluno e a nota do exame
            dados = linha.split()
            nome = dados[0]
            nota1 = float(dados[1])
            nota2 = float(dados[2])
            nota3 = float(dados[3])
            nota_exame = float(dados[4])
            media_anterior = float(dados[5]) if dados[5] != '-' else None

            # Calcular a nova média
            nova_media = calcular_media(nota1, nota2, nota3, nota_exame, media_anterior)

            # Verificar se o aluno está aprovado ou reprovado
            if nova_media >= 7:
                aprovados_file.write(f'{nome} {nova_media:.1f} Aprovado após exame\n')
            else:
                reprovados_file.write(f'{nome} {nova_media:.1f} Reprovado após exame\n')