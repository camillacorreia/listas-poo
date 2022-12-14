class Retangulo:
  def __init__(self):
    self.base = 0
    self.altura = 0
  def area(self):
    area = self.base*self.altura;
    print(area)
    return area
  def perimetro(self):
    perimetro = (self.base*2)+(self.altura*2);
    print(perimetro)
    return perimetro

### Testes
r = Retangulo()
r.base = 4
r.altura = 3
assert r.area() == 12
assert r.perimetro() == 14
r.base = 5
assert r.area() == 15
assert r.perimetro() == 16