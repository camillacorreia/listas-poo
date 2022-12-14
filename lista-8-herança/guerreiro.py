class Contador:
  def __init__(self, inicial):
    self._inicial = inicial
    self._contagem = inicial
  
  def decrementa(self, qtd=1):
    self._contagem -= qtd
    if self._contagem < 0:
      self._contagem = 0
  
  def reseta(self):
    self._contagem = self._inicial
  
  @property
  def contagem(self):
    return self._contagem

class Guerreiro:
  def __init__(self):
    self.contador = Contador(10)

  def recebe_dano(self):
    self.contador.decrementa(4)
  
  def provoca_dano(self, outro_guerreiro):
    if isinstance(outro_guerreiro, Guerreiro):
        outro_guerreiro.recebe_dano()
  
  @property
  def vida(self):
    return self.contador.contagem

### Testes
import unittest
from unittest import mock

class TestContaAuditada(unittest.TestCase):
  def test_guerreiro_tem_vida_10(self):
    g = Guerreiro()
    self.assertEqual(g.vida, 10)

  def test_guerreiro_nao_tem_vida_negativa(self):
    g = Guerreiro()
    g.recebe_dano()
    g.recebe_dano()
    g.recebe_dano()
    self.assertEqual(g.vida, 0)
    g.recebe_dano()
    self.assertEqual(g.vida, 0)

  def test_guerreiro_nao_reseta(self):
    g = Guerreiro()
    try:
      g.reseta()
      self.fail()
    except AttributeError:
      pass

  def test_guerreiro_nao_decrementa(self):
    g = Guerreiro()
    try:
      g.decrementa()
      self.fail()
    except AttributeError:
      pass

  @mock.patch('__main__.Contador.decrementa')
  def test_guerreiro_usa_contagem(self, decrementa):
    g = Guerreiro()
    g.recebe_dano()
    decrementa.assert_called()
  
  def test_guerreiro_nao_estende_contador(self):
    self.assertFalse(issubclass(Guerreiro, Contador))

if __name__ == '__main__':
  import sys
  unittest.main(exit=False)