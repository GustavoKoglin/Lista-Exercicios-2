def poupanca():
    return "poupanca.txt"

def mesAno():
    return "Mes/Ano:"

def inserir_salario():
    salario = float(input("Digite o valor mensal do seu salario: "))
    mes = input("Digite o mês do salario: ")
    ano = input("Digite o ano do salario: ")
    despesa = input("Digite a descricao da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    saldo_salario = salario - valor
    valor_poupar = salario * 0.1
    rendimento = valor_poupar * 0.01
    total_investido = valor_poupar * 12 * (1 + rendimento)**12

    with open(poupanca(), "a+") as arquivo:
        arquivo.write(f"Mes/Ano: {mes}/{ano}\nSalario: {salario}\nValor a poupar: {valor_poupar}\nTotal investido: {total_investido}\n Despesa: {despesa}\nValor da Despesa: {valor}\nSaldo do Salario: {saldo_salario}\n\n")

def alterar_salario():
    mes_ano = input("Digite o mês e ano do salario a ser alterado: (Ex: Janeiro/2021)")
    with open(poupanca(), "r") as arquivo:
        linhas = arquivo.readlines()
    with open(poupanca(), "w") as arquivo:
        for linha in linhas:
            if mes_ano in linha:
                salario = float(input("Digite o novo valor mensal do salario: "))
                valor_poupar = salario * 0.1
                rendimento = valor_poupar * 0.01
                total_investido = valor_poupar * 12 * (1 + rendimento)**12
                arquivo.write(f"Mes/Ano: {mes_ano}\nsalario: {salario}\nValor a poupar: {valor_poupar}\nTotal investido: {total_investido}\n")
            else:
                arquivo.write(linha)
            

def remover_salario():
    mes_ano = input("Digite o mês e ano do salario a ser removido: (Ex: Janeiro/2021) ")
    with open(poupanca(), "r") as arquivo:
        linhas = arquivo.readlines()
    with open(poupanca(), "w") as arquivo:
        removido = False
        for linha in linhas:
            if mes_ano in linha:
                removido = True
            else:
                arquivo.write(linha)
        if not removido:
            print("salario não encontrado.")

despesas = []

def listar_despesas():
    total = 0
    print("Lista de despesas:")
    for despesa in despesas:
        print(f"{despesa[mesAno()]} - {despesa['Descricao']} - R${despesa['Valor']:.2f}")
        total += despesa['Valor']
    print(f"Total de despesas: R${total:.2f}")

def alterar_despesa():
    mes_ano = input("Digite o mês/ano da despesa a ser alterada (MM/AAAA): ")
    for despesa in despesas:
        if despesa[mesAno()] == mes_ano:
            nova_descricao = input("Digite a nova descricao da despesa: ")
            novo_valor = float(input("Digite o novo valor da despesa: "))
            despesa['Descricao'] = nova_descricao
            despesa['Valor'] = novo_valor
            print("Despesa alterada com sucesso.")
            return
    print("Despesa não encontrada.")
    with open(poupanca(), "a+") as arquivo:
        arquivo.write(f"Mes/Ano: {mes_ano}\ndescricao: {despesa}\nValor: {despesa}\n")

def remover_despesa():
    mes_ano = input("Digite o mês/ano da despesa a ser removida (MM/AAAA): ")
    for despesa in despesas:
        if despesa[mesAno()] == mes_ano:
            despesas.remove(despesa)
            print("Despesa removida com sucesso.")
            return
    print("Despesa não encontrada.")

def verificar_meta_investimento():
    meta_investimento = float(input("Digite a meta de investimento: "))
    total_investido = 0
    for despesa in despesas:
        if despesa["Descricao"] == "Investimento":
            total_investido += float(despesa["Valor"])
    
    if total_investido >= meta_investimento:
        print("Parabéns! A meta de investimento foi batida.")
    else:
        print("A meta de investimento não foi batida.")

def encerrar_programa():
    print("Encerrando programa...")
    exit()

def exibir_menu():
    print("O sistema irá poupar '10%' do seu salario mensal para que possa ser investir. \n")
    print("-------- Menu --------")
    print("Selecione uma opção: \n")
    print("1 - Inserir salario")
    print("2 - Alterar salario")
    print("3 - Remover salario")
    print("4 - Alterar Despesa")
    print("5 - Remover Despesa")
    print("6 - Listar despesas")
    print("7 - Verificar se a meta de investimento foi batida")
    print("8 - Encerrar programa")

continuar = True
while continuar:
    exibir_menu()
    opcao = input("Digite sua escolha: ")
    if opcao == "1":
        inserir_salario()
    elif opcao == "2":
        alterar_salario()
    elif opcao == "3":
        remover_salario()
    elif opcao == "4":
        alterar_despesa()
    elif opcao == "5":
        remover_despesa()
    elif opcao == "6":
        listar_despesas()
    elif opcao == "7":
        verificar_meta_investimento()
    elif opcao == "8":
        encerrar_programa()
    else:
        print("Opção inválida. Tente novamente.")