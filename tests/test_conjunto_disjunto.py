import unittest
from exercicio_conjunto_disjunto import disjoint_set

class TestDisjointSet(unittest.TestCase):
    def test_disjoint_set(self):
        list1 = ['PSLL-123123', 'PSLL-123124', 'PSLL-123125', 'PSLL-123125', 'PSLL-123125']
        list2 = ['PSLL-123123', 'PSLL-123124', 'PSHH-151875', 'PSHH-111111', 'PSHH-987455', 'PSHH-432141']

        disjoint_tags = disjoint_set(list1, list2)
        expected_output = {'PSHH-987455', 'PSHH-111111', 'PSHH-151875', 'PSHH-432141'}

        # Convertendo as listas em conjuntos para verificar igualdade, independente da ordem
        disjoint_tags_set = set(disjoint_tags)
        expected_output_set = expected_output

        self.assertEqual(disjoint_tags_set, expected_output_set)

if __name__ == "__main__":
    unittest.main()
