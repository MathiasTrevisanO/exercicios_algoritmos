import queue

def main():
    fila_supermercado = queue.Queue()
    clientes_iniciais = ['cliente 1', 'cliente 2', 'cliente 3', 'cliente 4']
    for cliente in clientes_iniciais:
        fila_supermercado.put(cliente)
    print("Clientes iniciais:", list(fila_supermercado.queue))
    
    novos_clientes = ['cliente 5' , 'cliente 6' , 'cliente 7']
    for cliente in novos_clientes:
        fila_supermercado.put(cliente)
    print("Clientes adicionados:", list(fila_supermercado.queue))
    
    
    Cliente1 = fila_supermercado.get()
    Cliente2 = fila_supermercado.get()
    print(f"{Cliente1} e {Cliente2} atendidos")
    
    tamanho_fila = fila_supermercado.qsize()
    print("Tamanho da Fila atual:", tamanho_fila)

    clientes_adicionais = ['cliente 8', 'cliente 9']
    for cliente in clientes_adicionais:
        fila_supermercado.put(cliente)
    print("Clientes adicionados:", list(fila_supermercado.queue))
    
    while not fila_supermercado.empty():
        cliente = fila_supermercado.get()
        print(f"Atendendo o cliente: {cliente}")
    
    if fila_supermercado.empty():
        print("Fila de clientes está vazia")
    else:
        print("Ainda há clientes na fila")

if __name__ == '__main__':
    main()
