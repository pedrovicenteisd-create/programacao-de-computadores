x = int(input("Insira o primeiro número: "))
y = int(input("Insira o segundo número: "))
s = x+y
print("A soma entre x e y é: ",s)
if(x>y):
	print("x é maior que y")
elif(y>x):
	print("y é maior que x")
else:
	print("são iguais")
