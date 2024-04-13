import unittest

from exercicio_matriz_dinamica import create_matrix, sum_matrix, fill_matrix, print_matrix


class TestDynamicMatrix(unittest.TestCase):
    def test_create_matrix(self):
        
        matrix = create_matrix(2, 2)
        
        self.assertEqual(matrix[0][0], 0)
        self.assertEqual(matrix[0][1], 0)
        self.assertEqual(matrix[1][0], 0)
        self.assertEqual(matrix[1][1], 0)
        
        
    def test_print_matrix(self):
        matrix = create_matrix(2, 2)
        matrix[0][0] = 1
        matrix[0][1] = 2
        matrix[1][0] = 3
        matrix[1][1] = 4
        
        print_matrix(matrix)
    
    def test_sum_matrix(self):
        matrix = create_matrix(2, 2)
        matrix[0][0] = 1
        matrix[0][1] = 2
        matrix[1][0] = 3
        matrix[1][1] = 4
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] + matrix[i][j]
        
        self.assertEqual(matrix, [[2, 4], [6, 8]])

if __name__ == '__main__':
    unittest.main()

