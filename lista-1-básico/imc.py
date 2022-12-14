def esta_obesa(peso, altura):
  imc = peso/(altura*altura)
  print(imc)
  if imc >= 30:
    print("true")
    return True
  else:
    print("false")
    return False

esta_obesa(70, 1.70)
esta_obesa(170, 1.70)