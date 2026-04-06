x = int(input("Digite o valor de x: "))
if(x%2==0) and(x>0):
	print("Par positivo")
elif(x%2==0) and(x<0):
	print("Par negativo")
elif(x%2==1) and(x>0):
	print("Ímpar positivo")
elif(x%2==1) and(x<0):
	print("Ímpar negativo")
else:
	print("Neutro")
