import unittest

from exercicio_tabela_hash_encadeada import TableHash

class TestTableHash(unittest.TestCase):
    def test_insert_and_get(self):
        table = TableHash(10)
        table.insert("key1", "value1")
        table.insert("key2", "value2")
        
        self.assertEqual(table.get("key1"), "value1")
        self.assertEqual(table.get("key2"), "value2")
    
    def test_remove(self):
        table = TableHash(10)
        table.insert("key1", "value1")
        table.insert("key2", "value2")
        
        table.remove("key1")
        self.assertIsNone(table.get("key1"))
        self.assertEqual(table.get("key2"), "value2")
    
    def test_remove_nonexistent_key(self):
        table = TableHash(10)
        table.insert("key1", "value1")
        
        with self.assertRaises(KeyError):
            table.remove("key2")
    
    def test_get_nonexistent_key(self):
        table = TableHash(10)
        table.insert("key1", "value1")
        
        self.assertIsNone(table.get("key2"))
    
    def test_insert_same_key(self):
        table = TableHash(10)
        table.insert("key1", "value1")
        table.insert("key1", "value2")
        
        self.assertEqual(table.get("key1"), "value1")
    
    def test_large_hash_table(self):
        size = 1000
        table = TableHash(size)
        
        for i in range(size):
            table.insert(f"key{i}", f"value{i}")
        
        for i in range(size):
            self.assertEqual(table.get(f"key{i}"), f"value{i}")
    
if __name__ == '__main__':
    unittest.main()
