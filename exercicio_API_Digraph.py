from graphviz import Digraph

def criar_digrafo():
    # Criando o digrafo
    digraph = Digraph(format='png', engine='dot')

    # Adicionando os nós ao digrafo
    digraph.node('A')
    digraph.node('B')
    digraph.node('C')
    digraph.node('D')

    # Adicionando as arestas (dependências)
    digraph.edge('A', 'B')
    digraph.edge('A', 'C')
    digraph.edge('B', 'C')
    digraph.edge('C', 'D')

    # Renderizando o digrafo
    digraph.render('digraph', view=True)

if __name__ == "__main__":
    criar_digrafo()
