import re
from abc import ABC, abstractmethod

class Usuario(ABC):
  def __init__(self, matricula, nome):
    self._matricula = matricula
    self._nome = nome
  
  @abstractmethod
  def valida(self):
    pass
  
  def nome_normalizado(self):
    return self._nome.title()

class Aluno(Usuario):
  def valida(self):
    return re.match('^\\d{9}$', self._matricula)

class Servidor(Usuario):
  def valida(self):
    return re.match('^\\d{7}$', self._matricula)

### Testes
import unittest
from unittest import mock

class TestUsuario(unittest.TestCase):
  def test_validar_aluno(self):
    a = Aluno('200310593', 'Rodrigo')
    self.assertTrue(a.valida())
  
  def test_validar_servidor(self):
    s = Servidor('1973264', 'Rodrigo')
    self.assertTrue(s.valida())
  
  def test_nao_pode_instanciar_usuario(self):
    try:
      u = Usuario('123123', 'ABC')
      self.fail()
    except TypeError:
      pass

  def test_nova_classe_derivada(self):
    class AAA(Usuario):
        def __init__(self):
            pass
    try:
      u = AAA()
      self.fail()
    except TypeError:
      pass

if __name__ == '__main__':
  import sys
  unittest.main(exit=False)