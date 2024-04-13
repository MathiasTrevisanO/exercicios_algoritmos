import unittest

from exercicio_splay_tree import SplayTree

class TestSplayTree(unittest.TestCase):
    def test_insert_and_search(self):
        tree = SplayTree()
        keys = [100, 50, 200, 40, 30, 20, 25, 35]
        for key in keys:
            tree.insert(key)

        self.assertTrue(tree.search(20))
        self.assertTrue(tree.search(100))
        self.assertTrue(tree.search(35))
        self.assertFalse(tree.search(45))
        self.assertFalse(tree.search(300))

    def test_inorder_traversal(self):
        tree = SplayTree()
        keys = [100, 50, 200, 40, 30, 20, 25, 35]
        for key in keys:
            tree.insert(key)

        expected_inorder = [20, 25, 30, 35, 40, 50, 100, 200]
        self.assertEqual(tree.inorder_traversal(tree.root), expected_inorder)

if __name__ == "__main__":
    unittest.main()
