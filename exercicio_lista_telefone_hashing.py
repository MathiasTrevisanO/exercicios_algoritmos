class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class ListaTelefonica(Contato):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
    
    def hash_function(self, telefone):
        return sum([int(digit) for digit in telefone]) % self.tamanho
        
    def adicionar_contato(self, nome, telefone):
        index = self.hash_function(telefone)
        novo_contato = Contato(nome, telefone)
        self.tabela[index].append(novo_contato)
        
    def buscar_contato(self, telefone):
        index = self.hash_function(telefone)
        for contato in self.tabela[index]:
            if contato.telefone == telefone:
                return contato.nome
        return None
    
    def remover_contato(self, telefone):
        index = self.hash_function(telefone)
        for i, contato in enumerate(self.tabela[index]):
            if contato.telefone == telefone:
                del self.tabela[index][i]
                return True
        return False
    
def main():
    lista_telefonica = ListaTelefonica(10)

    lista_telefonica.adicionar_contato("João", "11999999999")
    lista_telefonica.adicionar_contato("Maria", "22999999999")
    lista_telefonica.adicionar_contato("Pedro", "33999999999")
    
    print(lista_telefonica.buscar_contato("11999999999"))
    print(lista_telefonica.buscar_contato("33999999999"))
    
    lista_telefonica.remover_contato("11999999999")
    
    print(lista_telefonica.buscar_contato("11999999999"))
    
if __name__ == "__main__":
    main()