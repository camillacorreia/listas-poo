class Retangulo:
  def __init__(self, b, a):
    self.base = b
    self.altura = a
  def altera_dimensoes(self, b, a):
    self.base = b
    self.altura = a
  def area(self):
    area = self.base*self.altura;
    print(area)
    return area
  def perimetro(self):
    perimetro = (self.base*2)+(self.altura*2);
    print(perimetro)
    return perimetro

### Testes
r = Retangulo(3, 4)
assert r.area() == 12
r.base = 5
assert r.area() == 20