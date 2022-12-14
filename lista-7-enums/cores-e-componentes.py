from enum import Enum

class Componente(Enum):
  RED = 'r'
  GREEN = 'g'
  BLUE = 'b'

class Cor:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b
  
  def altera(self, componente, valor):
    if componente == Componente.RED:
      self.r = valor
    elif componente == Componente.GREEN:
      self.g = valor
    elif componente == Componente.BLUE:
      self.b = valor

  def __eq__(self, o):
    return self.r == o.r and self.g == o.g and self.b == o.b

### Testes
c = Cor(1, 2, 3)
c.altera(Componente.RED, 128)
assert c.r == 128 and c.g == 2 and c.b == 3
c = Cor(1, 2, 3)
c.altera(Componente.GREEN, 100)
assert c.r == 1 and c.g == 100 and c.b == 3

c = Cor(1, 2, 3)
c.altera(Componente.BLUE, 255)
assert c.r == 1 and c.g == 2 and c.b == 255

assert isinstance(Componente.RED, Enum)