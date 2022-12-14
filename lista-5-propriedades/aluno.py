class Aluno:
  pass

### Testes
import unittest
class TestAluno(unittest.TestCase):
  def test_iguais(self):
    a = Aluno('123', 'abc')
    b = Aluno('123', 'abc')
    self.assertEqual(a, b)
  
  def test_mesma_matricula_nome_diferente(self):
    a = Aluno('123', 'abc')
    b = Aluno('123', 'def')
    self.assertEqual(a, b)
  
  def test_diferentes(self):
    a = Aluno('123', 'abc')
    b = Aluno('124', 'abc')
    self.assertNotEqual(a, b)

  def test_pode_mudar_nome(self):
    a = Aluno('123', 'abc')
    a.nome = 'def'
    self.assertEqual(a.nome, 'def')
  
  def test_nao_pode_mudar_matricula(self):
    a = Aluno('123', 'abc')
    with self.assertRaises(AttributeError):
      a.matricula = '456'

if __name__ == '__main__':
  import sys
  unittest.main(exit=False)