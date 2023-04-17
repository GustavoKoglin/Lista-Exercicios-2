paises = ["Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Argentina", "Brasil", "Estados Unidos", "França", "Itália", "Japão", "Portugal", "Reino Unido", "Rússia", "Suécia", "Suíça", "Turquia", "Uruguai", "Venezuela"]

def posicao_do_pais(pais, lista_de_paises):
    for i in range(len(lista_de_paises)):
        if lista_de_paises[i] == pais:
            return i
    return f"O país {pais} não foi encontrado na lista."

pais_procurado = pais_digitado = input("Digite o nome de um país: ")
posicao = posicao_do_pais(pais_procurado, paises)
print(f"O país {pais_digitado} está na posição {posicao}ªRúss da lista de países.")