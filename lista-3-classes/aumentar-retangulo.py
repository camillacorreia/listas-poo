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

  def aumenta(self, outro):
    self.base += outro.base
    self.altura += outro.altura
    print(self.base)
    print(self.altura)

### Testes
r1 = Retangulo(4, 5)
r2 = Retangulo(1, 2)
r1.aumenta(r2)
assert r1.base == 5 and r1.altura == 7
assert r2.base == 1 and r2.altura == 2