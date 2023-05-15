import os
import datetime
import pandas as pd


def mes_ano():
    return "Mes/Ano"


PASTA_SALARIOS = "salarios"
ARQUIVO_POUPE = "poupanca.csv"
ARQUIVO_DESP = "despesas.csv"
COLUNAS_POUPE = [
    mes_ano(),
    "Salario",
    "Valor a poupar",
    "Total investido",
    "Despesa",
    "Valor da Despesa",
    "Saldo do Salario",
]
COLUNAS_DESP = [mes_ano(), "Descricao", "Valor"]


def criar_pasta_salarios():
    if not os.path.exists(PASTA_SALARIOS):
        os.mkdir(PASTA_SALARIOS)


def criar_arquivo_poupe():
    if not os.path.exists(ARQUIVO_POUPE):
        with open(ARQUIVO_POUPE, "w") as arquivo:
            arquivo.write(",".join(COLUNAS_POUPE) + "\n")


def criar_arquivo_desp():
    if not os.path.exists(ARQUIVO_DESP):
        with open(ARQUIVO_DESP, "w") as arquivo:
            arquivo.write(",".join(COLUNAS_DESP) + "\n")


def inserir_salario():
    salario = float(input("Digite o valor mensal do seu salario: "))
    mes_ano = input("Digite o mês/ano do salario (MM/AAAA): ")
    mes, ano = mes_ano.split("/")
    despesa = input("Digite a descricao da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    saldo_salario = salario - valor
    valor_poupar = salario * 0.1
    rendimento = valor_poupar * 0.01
    total_investido = valor_poupar * 12 * (1 + rendimento) ** 12

    criar_pasta_salarios()
    criar_arquivo_poupe()

    with open(ARQUIVO_POUPE, "a") as arquivo:
        arquivo.write(
            f"{mes_ano},{salario},{valor_poupar},{total_investido},{despesa},{valor},{saldo_salario}\n"
        )


def alterar_salario():
    mes_ano = input("Digite o mês/ano do salario a ser alterado (MM/AAAA): ")
    mes, ano = mes_ano.split("/")
    df = pd.read_csv(ARQUIVO_POUPE)
    filtro = (df["Mes/Ano"] == mes_ano)
    if filtro.any():
        salario = float(input("Digite o novo valor mensal do salario: "))
        valor_poupar = salario * 0.1
        rendimento = valor_poupar * 0.01
        total_investido = valor_poupar * 12 * (1 + rendimento)**12
        df.loc[filtro, ["Salario", "Valor a poupar", "Total investido"]] = [salario, valor_poupar, total_investido]
        df.to_csv(ARQUIVO_POUPE, index=False)
        print("Salario alterado com sucesso!")
    else:
        print("Salario não encontrado!")

def inserir_despesa():
    mes_ano = input("Digite o mês/ano da despesa (MM/AAAA): ")
    descricao = input("Digite a descricao da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    with open(ARQUIVO_DESP, "a") as arquivo:
        arquivo.write(f"{mes_ano}, {descricao}, {valor}\n")

def alterar_despesas():
    mes_ano = input("Digite o mês/ano das despesas a serem alteradas (MM/AAAA): ")
    mes, ano = mes_ano.split("/")
    df = pd.read_csv(ARQUIVO_DESP)
    filtro = (df["Mes/Ano"] == mes_ano)
    if filtro.any():
        novas_despesas = float(input("Digite o novo valor total das despesas: "))
        df.loc[filtro, "Total despesas"] = novas_despesas
        df.to_csv(ARQUIVO_DESP, index=False)
        print("Despesas alteradas com sucesso!")
    else:
        print("Despesas não encontradas!")

def remover_despesa():
    mes_ano = input("Digite o mês/ano da despesa a ser removida (MM/AAAA): ")
    tipo = input("Digite o tipo da despesa a ser removida: ")
    df = pd.read_csv(ARQUIVO_DESP)
    filtro = (df["Mes/Ano"] == mes_ano) & (df["Tipo"] == tipo)
    if filtro.any():
        df = df.loc[~filtro, :]
        df.to_csv(ARQUIVO_DESP, index=False)
        print("Despesa removida com sucesso!")
    else:
        print("Despesa não encontrada!")

def mostrar_poupanca():
    if not os.path.exists(ARQUIVO_POUPE):
        print("Nenhum salario cadastrado ainda!")
    else:
        df = pd.read_csv(ARQUIVO_POUPE)
        print(df)

def mostrar_despesas():
    if not os.path.exists(ARQUIVO_DESP):
        print("Nenhuma despesa cadastrada ainda!")
    else:
        df = pd.read_csv(ARQUIVO_DESP)
        print(df)

while True:
    print("="*7, "Menu", "="*7)
    print("1 - Inserir salario")
    print("2 - Alterar salario")
    print("3 - Inserir despesa")
    print("4 - Alterar despesa")
    print("5 - Remover despesa")
    print("6 - Mostrar poupanca")
    print("7 - Mostrar despesas")
    print("0 - Sair \n")

    opcao = input("Escolha uma opcao: ")
    if opcao == "1":
        inserir_salario()
    elif opcao == "2":
        alterar_salario()
    elif opcao == "3":
        inserir_despesa()
    elif opcao == "4":
        alterar_despesas()
    elif opcao == "5":
        remover_despesa()
    elif opcao == "6":
        mostrar_poupanca()
    elif opcao == "7":
        mostrar_despesas()        
    elif opcao == "0":
        break
    else:
        print("Opcao invalida!")