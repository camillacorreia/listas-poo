import math

class Vetor:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __eq__(self, o):
    return abs(self.x - o.x) < 0.001 and abs(self.y - o.y) < 0.001
  
  @classmethod
  def comAnguloETamanho(cls, angulo, tamanho):
    x = math.cos(angulo) * tamanho
    y = math.sin(angulo) * tamanho
    return Vetor(x,y)

  @classmethod
  def vertical(cls,y):
    return Vetor(0,y)

  @classmethod
  def horizontal(cls,x):
    return Vetor(x,0)
    
assert Vetor.comAnguloETamanho(math.pi / 3, 10) == Vetor(5, 8.66025)
assert Vetor.comAnguloETamanho(math.pi, 10) == Vetor.horizontal(-10)
assert Vetor.vertical(5) == Vetor(0, 5)
assert Vetor.horizontal(-3) == Vetor(-3, 0)