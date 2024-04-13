import unittest

def stack_sort(list):
    stack = []
    for value in list:
        stack.append(value)
    
    sorted_list = []
    
    while stack:
        value = stack.pop()
        index = 0
        while index < len(sorted_list) and value > sorted_list[index]:
            index += 1
        
        sorted_list.insert(index, value)
    
    return sorted_list

class TestStackSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(stack_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(stack_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(stack_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reversed_sorted_list(self):
        self.assertEqual(stack_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_multiple_of_three_sorted_list(self):
        self.assertEqual(stack_sort([3, 6, 9, 12, 15]), [3, 6, 9, 12, 15])

    def test_multiple_of_three_reversed_sorted_list(self):
        self.assertEqual(stack_sort([15, 12, 9, 6, 3]), [3, 6, 9, 12, 15])

    def test_random_list(self):
        self.assertEqual(stack_sort([2, 5, 1, 4, 7, 3, 6, 9, 11, 10, 8, 13, 15]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15])

if __name__ == '__main__':
    unittest.main()