import unittest
from exercicio_metodo_do_fisico_analise_amortizada import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_enqueue(self):
        self.q.enqueue(10)
        self.assertEqual(self.q.size(), 1)
        self.q.enqueue(20)
        self.assertEqual(self.q.size(), 2)
        self.q.enqueue(30)
        self.assertEqual(self.q.size(), 3)
    
    def test_dequeue(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.q.enqueue(30)
        self.assertEqual(self.q.dequeue(), 10)
        self.assertEqual(self.q.dequeue(), 20)
        self.assertEqual(self.q.dequeue(), 30)
    
    def test_size(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.q.enqueue(30)
        self.assertEqual(self.q.size(), 3)
    
    def test_amortized_cost(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.q.enqueue(30)
        self.q.enqueue(40)
        self.q.enqueue(50)
        self.assertEqual(self.q.amortized_cost, 0)
        self.q.enqueue(60)
        self.assertEqual(self.q.amortized_cost, 5)

if __name__ == '__main__':
    unittest.main()
