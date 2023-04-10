#pede um número inteiro
try:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        print(f"O número {num} é par.")
    #se o número for ímpar, o programa deve parar e mostrar uma mensagem de erro
    else:
        raise ValueError("O número digitado é ímpar. Por favor, digite um número par.")
    #pede para o usuário digitar S para continuar ou N para parar   
    
#se o usuário digitar um número ímpar, o programa deve parar e mostrar uma mensagem de erro
except ValueError as error:
    print(error)    