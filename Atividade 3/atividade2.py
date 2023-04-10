try:
    string = input("Digite uma string: ")
    if not string.isupper():
        raise ValueError("A string contém letras minúsculas. Por favor, digite apenas letras maiúsculas.")
    print("A string contém apenas letras maiúsculas.")
except ValueError as error:
    print(error)