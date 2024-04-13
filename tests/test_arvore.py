import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exercicio_arvore import BinaryTree, Node

class TestInOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.insert(50)
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(40)
        self.tree.insert(70)
        self.tree.insert(60)
        self.tree.insert(80)

    def test_in_order_traversal(self):
        expected_output = [20, 30, 40, 50, 60, 70, 80]
        actual_output = []

        def in_order_traversal_callback(value): 
            actual_output.append(value)

        self.tree.in_order_traversal(in_order_traversal_callback)

        self.assertEqual(expected_output, actual_output)
    
    def test_pre_order(self):
        expected_output = [50, 30, 20, 40, 70, 60, 80]
        actual_output = []
        
        def pre_order_traversal_callback(value):
            actual_output.append(value)
        
        self.tree.pre_order_traversal(pre_order_traversal_callback)
        
        self.assertEqual(expected_output, actual_output)
    
    def test_post_order(self):
        expected_output = [20, 40, 30, 60, 80, 70, 50]
        actual_output = []
        
        def post_order_traversal_callback(value):
            actual_output.append(value)
        
        self.tree.post_order_traversal(post_order_traversal_callback)
        
        self.assertEqual(expected_output, actual_output)
        
        

if __name__ == '__main__':
    unittest.main()
