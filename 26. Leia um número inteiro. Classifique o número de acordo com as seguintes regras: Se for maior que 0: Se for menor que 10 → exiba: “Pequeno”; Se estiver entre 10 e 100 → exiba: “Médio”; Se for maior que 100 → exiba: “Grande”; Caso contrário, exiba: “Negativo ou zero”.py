x = int(input("Insira o valor de x: "))
if(0<x) and(x<10):
  print("Pequeno")
elif(10<=x) and(x<=100):
  print("Médio")
elif(x>100):
  print("Grande")
else:
  print("Negativo ou zero")
