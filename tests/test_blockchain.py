import unittest
from exercicio_blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_initial_chain(self):
        self.assertEqual(len(self.blockchain.chain), 1)
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block['proof'], 100)
        self.assertEqual(genesis_block['previous_hash'], '1')

    def test_create_new_block(self):
        proof = 35293
        prev_hash = '56fa0750ee9cbc24032ea0336e8b7dfe478673d5e3eacc73143528d7c19540ad'
        block = self.blockchain.create_new_block(proof, prev_hash)
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(block['proof'], proof)
        self.assertEqual(block['previous_hash'], prev_hash)

    def test_add_transaction(self):
        self.assertEqual(len(self.blockchain.transactions_pending), 0)
        index = self.blockchain.add_transaction("Leticia", "Mathias", 1)
        self.assertEqual(index, 2)
        self.assertEqual(len(self.blockchain.transactions_pending), 1)

    def test_proof_of_work(self):
        last_proof = self.blockchain.last_block['proof']
        proof = self.blockchain.proof_of_work(last_proof)
        self.assertTrue(self.blockchain.validate_proof(last_proof, proof))

    def test_validate_chain(self):
        self.assertTrue(self.blockchain.validate_chain(self.blockchain.chain))

if __name__ == '__main__':
    unittest.main()
