class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(-1)


pilha = Stack()

def adicionar_fim():
    valor = input("Digite o valor a ser adicionado no fim da pilha: ")
    pilha.push(valor)

def remover_topo():
    removido = pilha.pop()
    if removido == None:
        print("A pilha está vazia")
    else:
        print("Valor removido:", removido)

def mostrar_pilha():
    print("Valores na pilha: ", pilha.items)

def encerrar_programa():
    print("Encerrando programa...")
    exit()

def exibir_menu():
    print("Selecione uma opção:")
    print("1 - Adicionar números no fim da pilha")
    print("2 - Remover números do topo da pilha")
    print("3 - Mostrar números da pilha")
    print("4 - Encerrar programa")

continuar = True
while continuar:
    exibir_menu()
    opcao = input("Digite sua escolha: ")
    if opcao == "1":
        adicionar_fim()
    elif opcao == "2":
        remover_topo()
    elif opcao == "3":
        mostrar_pilha()
    elif opcao == "4":
        encerrar_programa()
    else:
        print("Opção inválida. Tente novamente.")