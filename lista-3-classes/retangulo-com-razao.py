class Retangulo:
  
  def __init__(self, b, a):
    self.base = b
    self.altura = a

  @property
  def razao(self):
    return self.base / self.altura 
    
  @razao.setter
  def razao(self, valor):
    self._razao = valor
    self.altura = self.base / self._razao

### Testes
r = Retangulo(10, 5)
assert r.razao == 2
r.base = 20
assert r.razao == 4
r.razao = 1
assert r.base == 20 and r.altura == 20
r.razao = 0.5
assert r.base == 20 and r.altura == 40