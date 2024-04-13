import random

def polynomial_hash(tag_name, coefficients, m):
    hash_value = 0
    for i, char in enumerate(tag_name, 1):  # Começando em 1 para a primeira iteração
        coef_idx = (i - 1) % len(coefficients)  # Usando (i - 1) para o índice começar em 0
        hash_value += coefficients[coef_idx] * (ord(char) ** i)
    return hash_value % m

import unittest
from exercicio_hash_polinomial import polynomial_hash

class TestPolynomialHash(unittest.TestCase):
    def test_polynomial_hash(self):
        tag_name = "PSLLL-3123219"
        coefficients = [2, 3, 5, 7, 11, 13]
        m = 30
        expected_hash_value = 9
        actual_hash_value = polynomial_hash(tag_name, coefficients, m)
        self.assertEqual(expected_hash_value, actual_hash_value)

if __name__ == '__main__':
    unittest.main()
