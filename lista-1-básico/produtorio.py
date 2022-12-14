def produtorio(lista):
  if len(lista) == 0:
    resultado = 1
  else:
    resultado = 1
    for i in lista:
      resultado *= i
  print(resultado)
  return resultado

assert produtorio([]) == 1
assert produtorio([1, 2, 3]) == 6
assert produtorio([1, 0, 3]) == 0