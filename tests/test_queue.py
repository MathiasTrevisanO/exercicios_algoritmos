import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def test_main(self):
        fila_supermercado = Queue()
        clientes_iniciais = ['cliente 1', 'cliente 2', 'cliente 3', 'cliente 4']
        for cliente in clientes_iniciais:
            fila_supermercado.put(cliente)
        self.assertEqual(list(fila_supermercado.queue), clientes_iniciais)
        
        novos_clientes = ['cliente 5', 'cliente 6', 'cliente 7']
        for cliente in novos_clientes:
            fila_supermercado.put(cliente)
        self.assertEqual(list(fila_supermercado.queue), clientes_iniciais + novos_clientes)

        Cliente1 = fila_supermercado.get()
        Cliente2 = fila_supermercado.get()
        self.assertEqual(Cliente1, 'cliente 1')
        self.assertEqual(Cliente2, 'cliente 2')
        self.assertEqual(fila_supermercado.qsize(), 5)

        clientes_adicionais = ['cliente 8', 'cliente 9']
        for cliente in clientes_adicionais:
            fila_supermercado.put(cliente)
        self.assertEqual(fila_supermercado.qsize(),7)

if __name__ == '__main__':
    unittest.main()