class Stack:
    def __init__(self):
        self.items = []
        self.removed_items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.items.pop()
        self.removed_items.append(item)
        return item

    def show_added_sites(self):
        print("Sites adicionados:")
        for site in self.items:
            print(site)

    def show_removed_sites(self):
        print("Sites removidos:")
        for site in self.removed_items:
            print(site)


historico = Stack()

while True:
    print("Selecione uma opção:")
    print("1. Adicionar site")
    print("2. Remover site")
    print("3. Mostrar sites adicionados")
    print("4. Mostrar sites removidos")
    print("5. Encerrar programa")
    opcao = input("Opção escolhida: ")
    if opcao == "1":
        site = input("Insira o site visitado: ")
        if ".com" in site or ".com.br" in site or ".br" in site or ".org" in site:
            historico.push(site)
            print("Site adicionado:", site)
        else:
            print("URL inválida. Insira um endereço que contenha '.com', '.com.br', '.br' ou '.org'.")
    elif opcao == "2":
        removerSite = input("Insira o site a ser removido: ")
        if removerSite in historico.items:
            historico.items.remove(removerSite)
            print("Site removido com sucesso:", removerSite)
        else:
            print("Site não encontrado no histórico.")
    elif opcao == "3":
        historico.show_added_sites()
    elif opcao == "4":
        historico.show_removed_sites()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Insira uma opção válida (1, 2, 3, 4 ou 5).")

print("Histórico atualizado:", historico.items)