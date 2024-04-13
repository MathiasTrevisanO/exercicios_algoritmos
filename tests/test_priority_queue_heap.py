import unittest
from exercicio_priority_queue_Heap import k_largest_elements, k_min_elements


class TestKlargestAndSmallest(unittest.TestCase):

    def test_k_largest_elements(self):
        arr = [3, 10, 4, 7, 8, 20, 15]
        k = 3
        expected = [20, 15, 10]
        self.assertEqual(k_largest_elements(arr, k), expected)

    def test_k_min_elements(self):
        arr = [3, 10, 4, 7, 8, 20, 15]
        k = 3
        expected = [3, 4, 7]
        self.assertEqual(k_min_elements(arr, k), expected)


if __name__ == '__main__':
    unittest.main()