class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    
fila = Queue()
fila.enqueue("João")
fila.enqueue("Maria")
fila.enqueue("José")
fila.enqueue("Pedro")
fila.enqueue("Ana")
fila.enqueue("Paulo")
fila.enqueue("Carlos")
fila.enqueue("Ricardo")
fila.enqueue("Marcos")
fila.enqueue("Mariana")
fila.enqueue("Juliana")
fila.enqueue("Alice")
fila.enqueue("Bruno")
fila.enqueue("Rafael")
fila.enqueue("Rafaela")
fila.enqueue("Larissa")

print("Pessoas na fila:")
for item in fila.items:
    print(item)

removerPessoa = input("Digite o nome da pessoa que deseja remover da fila: ")

pessoasARemover = []
for item in fila.items:
    if item == removerPessoa:
        pessoasARemover.append(item)

if len(pessoasARemover) > 0:
    for pessoa in pessoasARemover:
        fila.items.remove(pessoa)
        print(pessoa, "foi removido da fila.")
    print("Fila atual: ", fila.items)
else:
    print("Essa pessoa não está na fila.")