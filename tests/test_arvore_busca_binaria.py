import unittest
from exercicio_arvore_de_busca_binaria import Node, BST

class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(17)

    def test_value_present(self):
        self.assertTrue(self.tree.verify_value(10))
        self.assertTrue(self.tree.verify_value(5))
        self.assertTrue(self.tree.verify_value(15))
        self.assertTrue(self.tree.verify_value(3))
        self.assertTrue(self.tree.verify_value(7))
        self.assertTrue(self.tree.verify_value(12))
        self.assertTrue(self.tree.verify_value(17))

    def test_value_not_present(self):
        self.assertFalse(self.tree.verify_value(2))
        self.assertFalse(self.tree.verify_value(6))
        self.assertFalse(self.tree.verify_value(11))
        self.assertFalse(self.tree.verify_value(16))
        self.assertFalse(self.tree.verify_value(20))

if __name__ == '__main__':
    unittest.main()
