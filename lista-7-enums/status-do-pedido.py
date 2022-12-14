from enum import Enum

class Status:
  RECEBIDO = 0
  PAGO = 1
  ENVIADO = 2
  ENTREGUE = 3

class Pedido:
  def __init__(self, valor):
    self.valor = valor
    self.status = Status.RECEBIDO

  def pagar(self, forma_de_pagamento):
    if self.status == Status.RECEBIDO:
        self.status = Status.PAGO
  
  def enviar(self, transportadora):
    if self.status == Status.PAGO:
        self.status = Status.ENVIADO
  
  def entregar(self):
    if self.status == Status.ENVIADO:
        self.status = Status.ENTREGUE
  
  def situacao(self):
    if self.status == Status.RECEBIDO:
        return 'recebido'
    elif self.status == Status.PAGO:
        return 'pago'
    elif self.status == Status.ENVIADO:
        return 'enviado'
    elif self.status == Status.ENTREGUE:
        return 'entregue'

### Testes
import unittest

class TestPedido(unittest.TestCase):
  def test_pedido_novo(self):
    p = Pedido(2)
    self.assertEqual(p.status, Status.RECEBIDO)
  
  def test_pedido_pago(self):
    p = Pedido(2)
    p.pagar('pix')
    self.assertEqual(p.status, Status.PAGO)

  def test_pedido_enviado(self):
    p = Pedido(2)
    p.enviar('ufbalog')
    self.assertEqual(p.status, Status.RECEBIDO)
    p.pagar('pix')
    p.enviar('ufbalog')
    self.assertEqual(p.status, Status.ENVIADO)

  def test_pedido_entregue(self):
    p = Pedido(2)
    p.entregar()
    self.assertEqual(p.status, Status.RECEBIDO)
    p.pagar('pix')
    p.entregar()
    self.assertEqual(p.status, Status.PAGO)
    p.enviar('ufbalog')
    p.entregar()
    self.assertEqual(p.status, Status.ENTREGUE)

  def test_situacao(self):
    p = Pedido(2)
    self.assertEqual(p.situacao(), 'recebido')
    p.pagar('pix')
    self.assertEqual(p.situacao(), 'pago')
    p.enviar('ufbalog')
    self.assertEqual(p.situacao(), 'enviado')
    p.entregar()
    self.assertEqual(p.situacao(), 'entregue')

  def test_enum(self):
    self.assertTrue(isinstance(Status.RECEBIDO, Status))
    self.assertTrue(isinstance(Status.RECEBIDO, Enum))

if __name__ == '__main__':
  import sys
  unittest.main(exit=False)