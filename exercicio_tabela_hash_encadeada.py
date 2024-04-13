class TableHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
    
    def get(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return None
        else:
            for k, v in self.table[index]:
                if k == key:
                    return v
            return None  # Retorna None se a chave não for encontrada
    
    def remove(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            raise KeyError("key not found in hash table")
        else:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    del self.table[index][i]
                    return
            raise KeyError("key not found in hash table")


def main():
    table = TableHash(10)
    table.insert("key1", "value1")
    table.insert("key2", "value2")
    
    print(table.get("key1"))
    table.remove("key2")
    
if __name__ == '__main__':
    main()