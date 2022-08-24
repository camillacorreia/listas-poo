def faixa_etaria(idade):
  if idade==0 or idade==1:
    print("bebê")
    return "bebê"
  elif idade>=2 and idade<=11:
    print("criança")
    return "criança"
  elif idade>=12 and idade<=17:
    print("adolescente")
    return "adolescente"
  else:
    print("adulta")
    return "adulta"

assert faixa_etaria(0) == "bebê"
assert faixa_etaria(1) == "bebê"
assert faixa_etaria(2) == "criança"
assert faixa_etaria(11) == "criança"
assert faixa_etaria(12) == "adolescente"
assert faixa_etaria(17) == "adolescente"
assert faixa_etaria(18) == "adulta"
assert faixa_etaria(81) == "adulta"