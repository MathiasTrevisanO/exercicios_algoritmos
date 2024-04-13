import unittest
import sys
import os

# Adicionando o diretório pai ao path para importar a classe Pilha
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exercicio_pilha import Pilha

class TestPilha(unittest.TestCase):
    def test_verificar_balanceamento_1(self):
        pilha = Pilha()
        expressao = '(()())'
        resultado = pilha.verificar_balanceamento(expressao)
        self.assertTrue(resultado)

    def test_verificar_balanceamento_2(self):
        pilha = Pilha()
        expressao = '()()'
        resultado = pilha.verificar_balanceamento(expressao)
        self.assertTrue(resultado)

    def test_verificar_balanceamento_3(self):
        pilha = Pilha()
        expressao = '(()'
        resultado = pilha.verificar_balanceamento(expressao)
        self.assertFalse(resultado)

    def test_verificar_balanceamento_4(self):
        pilha = Pilha()
        expressao = '())('
        resultado = pilha.verificar_balanceamento(expressao)
        self.assertFalse(resultado)

def main():
    pilha = Pilha()
    print("Digite a expressão de parenteses...")
    expressao = str(input())
    resultado = pilha.verificar_balanceamento(expressao)
    if resultado == True:
        print("A expressão está balanceada!")
    else:
        print("A expressão não está balanceada!")

if __name__ == "__main__":
    unittest.main()