def segundo_grau(x, a, b=0, c=0):
  y = a * (x ** 2) + b * x + c
  print(y)
  return y

### Testes
assert segundo_grau(2, 1, 1, 1) == 7
assert segundo_grau(3, 4, -2) == segundo_grau(3, 4, -2, 0)
assert segundo_grau(-2, 7) == segundo_grau(-2, 7, 0, 0)
assert segundo_grau(-2, 7, c=8) == segundo_grau(-2, 7, 0, 8)