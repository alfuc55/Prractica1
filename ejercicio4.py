import numpy
#Pedir un numero al usuario
a = int(input("ingresar un numero mayor a 1 :"))
# generar un rango de numeros entre 1 y el numero ingresado por el usuario
num = range(1,a+1)
# crear listas vacias para guardar los pares e impares
numP=[]
numI=[]
sumap=0
producto=1
# Blucle para determinar si el numero es par o impar
for i in num:
    # si es par
    if i%2== 0:
        # agregar el numero a la lista de pares
        numP.append(i)
        # varibale con la suma de los pares
        sumap = sumap + i
    # si es impar
    if i%2!=0:
        # agregar a la lista de impares
        numI.append(i)
        # calcular el producto
        producto = producto*i
print("Promedio de numeros pares")
print("(", end="")
# imprimir los resutlados de la suma de pares
for i in range(len(numP)):
    if i != len(numP)-1:
        print(numP[i], "+ ", end="")
    else:
        print(numP[i], ")", "/",len(numP), " = " ,end="")
promedio = sumap/len(numP)
print(promedio)
# imprimir los resutlados del producto de impares
print("Producto de numeros impares")
print("(", end="")
for i in range(len(numI)):
    if i != len(numP)-1:
        print(numI[i], "*", end="")
    else:
        print(numI[i], ")", " = " ,end="")
print(producto)
