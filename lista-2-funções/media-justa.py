def maior(lista):
  if len(lista)==0:
    return 0
  else:
    maior_elemento = max(lista)
    return (maior_elemento)

def media_justa(lista):
  maior_numero = maior(lista)
  if maior_numero==0 or len(lista)==1:
    return 0
  else:
    cont = 0
    soma=0
    for item in lista:
      if maior_numero == item and cont == 0:
        cont=1
      else:
        soma+=item
    media = soma/(len(lista)-1)
    return media

### Testes
assert maior([]) == 0
assert maior([4]) == 4
assert maior([3, 5, 2]) == 5
assert maior([8, 3, 5, 2]) == 8
assert maior([8, 3, 5, 9]) == 9

assert media_justa([]) == 0
assert media_justa([6]) == 0
assert media_justa([12, 18]) == 12
assert media_justa([1, 3, 5]) == 2

from unittest.mock import MagicMock
maior = MagicMock(return_value=5)
assert media_justa([5, 10]) == 10
maior.assert_called()