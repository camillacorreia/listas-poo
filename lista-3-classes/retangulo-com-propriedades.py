class Retangulo:
  
  def __init__(self, b, a):
    self.base = b
    self.altura = a

  @property
  def area(self):
    self.__area = self.base * self.altura
    return self.__area
  

### Testes
r1 = Retangulo(3, 4)
assert r1.area == 12

r1.base = 5
r1.altura = 3
assert r1.area == 15

houve_excecao = False
try:
  r1.area = 10
except AttributeError as e:
  houve_excecao = True
assert houve_excecao