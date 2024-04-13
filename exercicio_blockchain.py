import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions_pending = []
        
        self.create_new_block(proof=100, old_hash='1')
        
    def create_new_block(self, proof, old_hash=None):
        if not old_hash and not self.chain:
            old_hash = '1'
        elif not old_hash:
            old_hash = self.hash(self.chain[-1])

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions_pending,
            'proof': proof,
            'previous_hash': old_hash,
        }
        
        self.transactions_pending = []
        self.chain.append(block)
        return block
    
    def add_transaction(self, sender, recipient, value):
        self.transactions_pending.append({
            'sender': sender,
            'recipient': recipient,
            'value': value
        })
        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block):
        block_string = str(block)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, last_proof):
        new_proof = 0
        while self.validate_proof(last_proof, new_proof) is False:
            new_proof += 1
        return new_proof
    
    @staticmethod
    def validate_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    def validate_chain(self, chain):
        last_block = chain[0]
        actual_index = 1  # Começando a partir do segundo bloco
        
        while actual_index < len(chain):
            block = chain[actual_index]

            if block['previous_hash'] != self.hash(last_block):
                print(f"Invalid hash for block {block['index']}")
                return False

            if not self.validate_proof(last_block['proof'], block['proof']):
                print(f"Invalid proof of work for block {block['index']}")
                return False

            last_block = block
            actual_index += 1

        return True
    
if __name__ == "__main__":
    blockchain = Blockchain()
    
    print("Mining Block 1...")
    blockchain.add_transaction("Leticia", "Mathias", 1)
    proof = blockchain.proof_of_work(blockchain.last_block['proof'])
    prev_hash = blockchain.hash(blockchain.last_block)
    block1 = blockchain.create_new_block(proof, prev_hash)
    print("Block 1 mined:", block1)
    
    print("Mining Block 2...")
    blockchain.add_transaction("Mathias", "Josué", 2)
    proof = blockchain.proof_of_work(blockchain.last_block['proof'])
    prev_hash = blockchain.hash(block1)
    block2 = blockchain.create_new_block(proof, prev_hash)
    print("Block 2 mined:", block2)
    
    print("Mining Block 3...")
    blockchain.add_transaction("Josué", "Lucas", 3)
    proof = blockchain.proof_of_work(blockchain.last_block['proof'])
    prev_hash = blockchain.hash(block2)
    block3 = blockchain.create_new_block(proof, prev_hash)
    print("Block 3 mined:", block3)
    
    print("Blockchain:")
    for block in blockchain.chain:
        print(block)
        
    print("Blockchain is valid:", blockchain.validate_chain(blockchain.chain))
