class ComprimentoDiferente(Exception):
    pass

try:
    str1 = input("Digite a primeira string: ")
    str2 = input("Digite a segunda string: ")
    if len(str1) != len(str2):
        raise ComprimentoDiferente("Erro: As strings possuem comprimentos diferentes.")
    else:
        print("As strings possuem o mesmo comprimento.")
except ComprimentoDiferente as e:
    print(e)