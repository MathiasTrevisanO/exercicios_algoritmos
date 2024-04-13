import hashlib

def calculate_hash(transaction):
    return hashlib.sha256(transaction.encode()).hexdigest()

def build_merkle_tree(transactions):
    if len(transactions) == 0:
        return None
    
    hashes = [calculate_hash(transaction) for transaction in transactions]
    
    while len(hashes) > 1:
        new_hashes = []
        for i in range(0, len(hashes), 2):
            if i+1 == len(hashes):
                new_hash = hashlib.sha256((hashes[i] + hashes[i]).encode()).hexdigest()
            else:
                new_hash = hashlib.sha256((hashes[i] + hashes[i+1]).encode()).hexdigest()
            new_hashes.append(new_hash)
        hashes = new_hashes
    
    return hashes[0]

def main():
    transactions  = [
        "10 BTC de A para B",
        "5 BTC de C para D",
        "3 BTC de E para F",
        "7 BTC de G para H"
    ]
    
    merkle_root = build_merkle_tree(transactions)
    
    print("Root of Merkle Tree:", merkle_root)

if __name__ == '__main__':
    main()