import unittest
import hashlib
from exercicio_arvore_de_Merkle import build_merkle_tree


class TestMerkleTree(unittest.TestCase):
    def test_empty_transactions(self):
        transactions = []
        merkle_root = build_merkle_tree(transactions)
        self.assertIsNone(merkle_root, "Merkle root should be None for empty transactions")
    
    def test_merkle_root(self):
        transactions = [
            "10 BTC de A para B",
            "5 BTC de C para D",
            "3 BTC de E para F",
            "7 BTC de G para H"
        ]
        expected_merkle_root = "b4c0192b1e113f1936aac4fac784beb7f51b33f6cd5e6ccc1657e980964ac1b2"
        merkle_root = build_merkle_tree(transactions)
        self.assertEqual(merkle_root, expected_merkle_root, "Merkle root calculation incorrect")

if __name__ == '__main__':
    unittest.main()
