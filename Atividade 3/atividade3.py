try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print("Resultado da divisão: ", resultado)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Digite um número inteiro válido.")