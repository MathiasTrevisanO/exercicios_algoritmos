import unittest
from exercicio_arvore_AVL import AVLTree

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl_tree = AVLTree()

    def test_tree_construction(self):
        myTree = AVLTree()
        root = None
        
        root = myTree.insert(root, 10)
        root = myTree.insert(root, 20)
        root = myTree.insert(root, 30)
        root = myTree.insert(root, 40)
        root = myTree.insert(root, 50)
        root = myTree.insert(root, 25)
        
        expected_preorder = [30, 20, 10, 25, 40, 50]
        result = myTree.preOrder(root)
        self.assertEqual(result, expected_preorder)

if __name__ == "__main__":
    unittest.main()
