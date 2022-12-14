def retangulo(caractere, base, altura):
  ret = ""
  for i in range(altura):
    if altura == 0:
      return ret
    if altura == 1:
      ret = (caractere * base)
      return ret
    else:
      if i == 0:
        ret = (caractere * base) + "\n"
      elif i == altura - 1:
        ret = ret + (caractere * base)
      else:
        ret = ret + (caractere + (" " * (base - 2) + caractere)) + "\n"
  print(ret)
  return ret

### Testes
assert retangulo("*", 4, 2).strip() == "****\n****"
assert retangulo("#", 5, 1).strip() == "#####"