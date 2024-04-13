import unittest
from exercicio_lista_telefone_hashing import Contato, ListaTelefonica

class TestListaTelefonica(unittest.TestCase):
    def setUp(self):
        self.lista_telefonica = ListaTelefonica(10)
        self.contato1 = Contato("Maria", "1234567890")
        self.contato2 = Contato("João", "9876543210")
        self.contato3 = Contato("Ana", "5555555555")
        
    def test_adicionar_contato(self):
        self.lista_telefonica.adicionar_contato(self.contato1.nome, self.contato1.telefone)
        self.lista_telefonica.adicionar_contato(self.contato2.nome, self.contato2.telefone)
        self.lista_telefonica.adicionar_contato(self.contato3.nome, self.contato3.telefone)
        self.assertEqual(self.lista_telefonica.buscar_contato("1234567890"), "Maria")
        self.assertEqual(self.lista_telefonica.buscar_contato("9876543210"), "João")
        self.assertEqual(self.lista_telefonica.buscar_contato("5555555555"), "Ana")
    
    def test_adicionar_contato_duplicado(self):
        self.lista_telefonica.adicionar_contato(self.contato1.nome, self.contato1.telefone)
        self.lista_telefonica.adicionar_contato(self.contato2.nome, self.contato2.telefone)
        self.lista_telefonica.adicionar_contato(self.contato1.nome, self.contato1.telefone)
        self.lista_telefonica.adicionar_contato(self.contato3.nome, self.contato3.telefone)
        # Apenas os contatos únicos devem estar na lista
        self.assertEqual(self.lista_telefonica.buscar_contato("1234567890"), "Maria")
        self.assertEqual(self.lista_telefonica.buscar_contato("9876543210"), "João")
        self.assertEqual(self.lista_telefonica.buscar_contato("5555555555"), "Ana")
        
    def test_remove_contato(self):
        self.lista_telefonica.adicionar_contato(self.contato1.nome, self.contato1.telefone)
        self.lista_telefonica.adicionar_contato(self.contato2.nome, self.contato2.telefone)
        self.lista_telefonica.adicionar_contato(self.contato3.nome, self.contato3.telefone)
        self.lista_telefonica.remover_contato(self.contato2.telefone)
        self.assertEqual(self.lista_telefonica.buscar_contato("9876543210"), None)
    
    def test_remove_contato_inexistente(self):
        self.lista_telefonica.adicionar_contato(self.contato1.nome, self.contato1.telefone)
        self.lista_telefonica.adicionar_contato(self.contato2.nome, self.contato2.telefone)
        self.lista_telefonica.adicionar_contato(self.contato3.nome, self.contato3.telefone)
        # Tenta remover um contato que não está na lista, nada deve mudar
        contato_inexistente = Contato("Inexistente", "9999999999")
        self.lista_telefonica.remover_contato(contato_inexistente.telefone)
        # Verifica se os contatos ainda estão na lista
        self.assertEqual(self.lista_telefonica.buscar_contato("1234567890"), "Maria")
        self.assertEqual(self.lista_telefonica.buscar_contato("9876543210"), "João")
        self.assertEqual(self.lista_telefonica.buscar_contato("5555555555"), "Ana")
    
    
if __name__ == '__main__':
    unittest.main()
