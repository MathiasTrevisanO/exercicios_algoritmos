import unittest
from exercicio_filas_prioritarias import add_pacient, attend_pacient
import queue

class TestHospitalQueue(unittest.TestCase):
    def setUp(self):
        self.priority_queue = queue.PriorityQueue()

    def test_add_pacient(self):
        add_pacient(self.priority_queue, 'A')
        add_pacient(self.priority_queue, 'B')
        add_pacient(self.priority_queue, 'C')

        self.assertEqual(self.priority_queue.qsize(), 3)

    def test_attend_pacient(self):
        add_pacient(self.priority_queue, 'A')
        add_pacient(self.priority_queue, 'B')
        add_pacient(self.priority_queue, 'C')

        attend_pacient(self.priority_queue)

        self.assertEqual(self.priority_queue.qsize(), 0)

if __name__ == '__main__':
    unittest.main()
