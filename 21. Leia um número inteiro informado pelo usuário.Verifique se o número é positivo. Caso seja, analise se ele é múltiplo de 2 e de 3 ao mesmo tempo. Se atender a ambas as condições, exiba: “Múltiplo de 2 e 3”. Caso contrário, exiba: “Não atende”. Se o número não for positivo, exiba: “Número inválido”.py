x = int(input("Insira o valor de x: "))
if(x%2==0) and(x%3==0)and(x>0):
	print("Múltiplo de 2 e 3")
elif(x<0):
	print("Número inválido")
else:
	print("Não atende")
