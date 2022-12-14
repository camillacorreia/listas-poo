class Retangulo:
  def __init__(self):
    self.base = 0
    self.altura = 0
  def altera_dimensoes(self, b, a):
    self.base = b
    print(self.base)
    self.altura = a
    print(self.altura)

### Testes
r = Retangulo()
r.altera_dimensoes(23, 76)
assert r.base == 23
assert r.altura == 76