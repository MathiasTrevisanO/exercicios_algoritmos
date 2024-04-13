import unittest
import pandas as pd
from exercicio_Rabin_Karp import rabin_karp
import os

class TestRabinKarp(unittest.TestCase):

    def test_rabin_karp(self):
        # Obtém o diretório do script atual
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, "..", "") #Set any csv file to search a key
        
        # Lê o arquivo CSV
        text = pd.read_csv(csv_path, sep=";")
        
        pattern1 = "ZSH_5262631"
        self.assertIn(pattern1, [line[0] for line in rabin_karp(text.values.tolist(), pattern1)])
        
        pattern2 = "XS_5148511"
        self.assertIn(pattern2, [line[0] for line in rabin_karp(text.values.tolist(), pattern2)])

        pattern3 = "PIT_5241534"
        self.assertIn(pattern3, [line[0] for line in rabin_karp(text.values.tolist(), pattern3)])
    
if __name__ == '__main__':
    unittest.main()
