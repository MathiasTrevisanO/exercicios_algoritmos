import unittest
import heapq

def heap_sort(array):
    heapq.heapify(array)
    sorted_array = []
    while array:
        sorted_array.append(heapq.heappop(array))

    return sorted_array


class TestHeapSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_one_element_list(self):
        self.assertEqual(heap_sort([1]), [1])

    def test_even_number_list(self):
        self.assertEqual(heap_sort([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_odd_number_list(self):
        self.assertEqual(heap_sort([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()