def sequencia(N):
  lista = []
  if N > 0:
    for i in range(1,N+1):
      lista.append(i)
  print(lista)
  return(lista)

assert sequencia(3) == [1, 2, 3]
assert sequencia(1) == [1]
assert sequencia(-1) == []