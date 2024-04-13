import unittest
from exercicio_priority_queue_disjoint_set import UnionFindPriority

class TestUnionFindPriority(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFindPriority(6)
        self.uf.union(0, 1)
        self.uf.union(1, 2)
        self.uf.union(3, 4)

    def test_find(self):
        # Verifica se os líderes estão corretos após as uniões
        self.assertEqual(self.uf.find(0), 0)  # Deve ser o líder do conjunto que contém 0
        self.assertEqual(self.uf.find(1), 1)  # Deve ser o líder do conjunto que contém 1
        self.assertEqual(self.uf.find(2), 2)  # Deve ser o líder do conjunto que contém 2
        self.assertEqual(self.uf.find(3), 3)  # Deve ser o líder do conjunto que contém 3
        self.assertEqual(self.uf.find(4), 4)  # Deve ser o líder do conjunto que contém 4

    def test_union(self):
        # Testa uniões adicionais e verifica se os líderes estão corretos após as novas uniões
        self.uf.union(0, 3)
        self.assertEqual(self.uf.find(0), 0) # Deve ser o líder do conjunto que contém 0 após a nova união
        self.assertEqual(self.uf.find(3), 3)  # Deve ser o líder do conjunto que contém 3 após a nova união
        self.uf.union(2, 5)
        self.assertEqual(self.uf.find(2), 2)  # Deve ser o líder do conjunto que contém 2 após a nova união
        self.assertEqual(self.uf.find(5), 5)  # Deve ser o líder do conjunto que contém 5 após a nova união

        # Teste de união com valores não conectados
        self.uf.union(1, 4)
        self.assertEqual(self.uf.find(1), 1)  # Deve ser o líder do conjunto que contém 1 após a nova união
        self.assertEqual(self.uf.find(4), 4)  # Deve ser o líder do conjunto que contém 4 após a nova união

if __name__ == '__main__':
    unittest.main()
