class Cor:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b
  
  def __eq__(self, o):
    return self.r == o.r and self.g == o.g and self.b == o.b

class Paleta:
  AZUL = Cor(0,0,255)
  VERMELHA = Cor(255,0,0)
  AMARELA = Cor(255,255,0)

### Testes

assert Paleta.AZUL.b == 255 and Paleta.AZUL.r == 0 and Paleta.AZUL.g == 0
assert Paleta.VERMELHA == Cor(255, 0, 0)
assert Paleta.AMARELA == Cor(255, 255, 0)