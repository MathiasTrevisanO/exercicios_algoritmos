
class Pilha:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items) - 1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def verificar_balanceamento(self, expressao):
        for item in expressao:
            if item == '(':
                self.push(item) 
            elif item == ')':
                if not self.is_empty() and self.top() == '(': 
                    self.pop()
                else:
                    return False
        return self.is_empty()

def main():
    pilha = Pilha()
    print("Digite a expressão de parenteses...")
    expressao = str(input())
    resultado = pilha.verificar_balanceamento(expressao)
    if resultado == True:
        print("A expressão está balanceada!")
    else:
        print("A expressão não está balanceada!")

if __name__ == "__main__":
    main()