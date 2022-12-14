import math

def distancia(x1, y1, x2, y2):
  """Calcula a distância euclideana entre os pontos (x1, y1) e (x2, y2).
  """
  A = x2-x1;
  B = y2-x2;
  res = ((A*A)+(B*B))/2;
  print(res)
  return res
### Testes
assert distancia(2, 2, 5, 6) == 5
assert distancia.__doc__ is not None