class Pedido:
  RECEBIDO = 0
  PAGO = 1
  ENVIADO = 2
  ENTREGUE = 3
  
  def __init__(self, valor):
    self.valor = valor
    self.status = 0

  def pagar(self, forma_de_pagamento):
    if self.status == Pedido.RECEBIDO:
        self.status = Pedido.PAGO
  
  def enviar(self, transportadora):
    if self.status == Pedido.PAGO:
        self.status = Pedido.ENVIADO
  
  def entregar(self):
    if self.status == Pedido.ENVIADO:
        self.status = Pedido.ENTREGUE

### Testes
import unittest

class TestPedido(unittest.TestCase):
  def test_pedido_novo(self):
    p = Pedido(2)
    self.assertEqual(p.status, Pedido.RECEBIDO)
  
  def test_pedido_pago(self):
    p = Pedido(2)
    p.pagar('pix')
    self.assertEqual(p.status, Pedido.PAGO)

  def test_pedido_enviado(self):
    p = Pedido(2)
    p.enviar('ufbalog')
    self.assertEqual(p.status, Pedido.RECEBIDO)
    p.pagar('pix')
    p.enviar('ufbalog')
    self.assertEqual(p.status, Pedido.ENVIADO)

  def test_pedido_entregue(self):
    p = Pedido(2)
    p.entregar()
    self.assertEqual(p.status, Pedido.RECEBIDO)
    p.pagar('pix')
    p.entregar()
    self.assertEqual(p.status, Pedido.PAGO)
    p.enviar('ufbalog')
    p.entregar()
    self.assertEqual(p.status, Pedido.ENTREGUE)

  def test_codigos_numericos(self):
    self.assertEqual(Pedido.RECEBIDO, 0)
    self.assertEqual(Pedido.PAGO, 1)
    self.assertEqual(Pedido.ENVIADO, 2)
    self.assertEqual(Pedido.ENTREGUE, 3)

if __name__ == '__main__':
  import sys
  unittest.main(exit=False)