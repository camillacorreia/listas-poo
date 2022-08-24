def linha(c, n):
  palavra = ''
  for i in range(n):
    palavra = palavra + c
  return palavra

assert linha("*", 5) == "*****"
assert linha("#", 2) == "##"
assert linha("@", 0) == ""