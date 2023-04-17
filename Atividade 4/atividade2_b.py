class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)


fila = Queue()

while True:
    print("1 - Adicionar número à fila")
    print("2 - Remover primeiro número da fila")
    print("3 - Sair do programa")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        numero = int(input("Digite o número que deseja adicionar: "))
        fila.enqueue(numero)
        print("Número adicionado à fila.")
        print("Fila atual:", fila.items)

    elif opcao == "2":
        if fila.is_empty():
            print("A fila está vazia.")
        else:
            numero = fila.dequeue()
            print(f"O número {numero} foi removido da fila.")
            print("Fila atual:", fila.items)

    elif opcao == "3":
        break

    else:
        print("Opção inválida. Tente novamente.")