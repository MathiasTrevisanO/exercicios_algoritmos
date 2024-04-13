import unittest
from queue import Queue
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exercicio_metodo_agregado_analise_amortizada import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_dequeue(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.dequeue(1)
        self.assertEqual(self.q.size, 2)
        self.q.dequeue(2)
        self.q.dequeue(3)
        self.assertEqual(self.q.size, 0)
    
    def test_enqueue(self):
        self.q.enqueue(1)
        self.assertEqual(self.q.size, 1)
        self.q.enqueue(2)
        self.assertEqual(self.q.size, 2)
        self.q.enqueue(3)
        self.assertEqual(self.q.size, 3)   
         
        

if __name__ == '__main__':
    unittest.main()