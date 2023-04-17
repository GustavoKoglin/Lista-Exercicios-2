listaInicio = []
listaFim = []

entradaInicio = input("Digite um número inteiro para a lista inicial. (Ou 'fim' para continuar para a lista final): ")
while entradaInicio.upper() != 'FIM':
    numero1 = int(entradaInicio)
    listaInicio.append(numero1)
    entradaInicio = input("Digite um número inteiro para a lista inicial. (Ou 'fim' para continuar para a lista final): ")

entradaFim = input("Digite um número inteiro para a lista final, (ou 'fim' para encerrar): ")
while entradaFim.upper() != 'FIM':
    numero2 = int(entradaFim)
    listaFim.append(numero2)
    entradaFim = input("Digite um número inteiro para a lista final, (ou 'fim' para encerrar): ")

print(listaInicio, listaFim)