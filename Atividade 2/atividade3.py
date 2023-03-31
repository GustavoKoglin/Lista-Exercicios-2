# Abrir arquivo de exame
with open('exame.txt', 'r') as file:
    exame_data = file.readlines()

# Abrir arquivo de notas
with open('notas.txt', 'r') as file:
    notas_data = file.readlines()

# Criar dicionário para armazenar notas dos alunos do exame
exame_notas = {}
for line in exame_data:
    aluno, nota = line.strip().split(':')
    exame_notas[aluno] = float(nota)

# Criar dicionário para armazenar notas dos alunos das notas gerais
notas_alunos = {}
for line in notas_data:
    aluno, nota1, nota2, nota3 = line.strip().split(',')
    notas_alunos[aluno] = [float(nota1), float(nota2), float(nota3)]

# Calcular média das notas gerais dos alunos
media_alunos = {}
for aluno, notas in notas_alunos.items():
    media_aluno = sum(notas) / len(notas)
    media_alunos[aluno] = media_aluno

# Atualizar médias dos alunos que fizeram exame
for aluno, nota in exame_notas.items():
    media_anterior = media_alunos[aluno]
    nova_media = (media_anterior * 3 + nota) / 4
    media_alunos[aluno] = nova_media

    # Verificar se o aluno foi aprovado ou reprovado
    if nova_media >= 5:
        with open('aprovados.txt', 'a') as file:
            file.write(f'{aluno}: {nova_media:.2f} - Aprovado após exame\n')
    else:
        with open('reprovados.txt', 'a') as file:
            file.write(f'{aluno}: {nova_media:.2f} - Reprovado após exame\n')