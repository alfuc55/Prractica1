import random
def imprimir():
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print(" ")
def derecha(i1, j1): 
    i=i1
    j=j1
    while a[i1][j1]!=["X"] and j1 < m-1:
        if a[i1][j1+1] == ["X"]:
            return i1, j1
            break
        elif j1 == 4:
            a[i1][j1] = ["->"]
            return i1, j1
        else:
            a[i1][j1] = ["->"]
        j1 = j1+1
        # regresar j
    return i1, j1

def abajo(i1, j1):
    i=i1
    j=j1 # anterior 
    while a[i1][j1]!=["X"] and i1 < n-1:
        if a[i1+1][j1] == ["X"]:
            return i1, j1
            break
        elif i1==4:
            a[i1][j1]=["V"]
            return i1,j1
        else:
            a[i1][j1]=["V"]
        i1 = i1+1
        # regresar i
    return i1, j1
def izquierda(i1, j1): 
    i=i1 # anterior 
    j=j1 # anterior 
    while a[i1][j1]!=["X"] and j1 >= 0:
        if a[i1][j1-1] == ["X"]:
            return i1, j1
            break
        elif j1 == 0:
            a[i1][j1] = ["<-"]
            return i1, j1
        else:
            a[i1][j1] = ["<-"]
        j1 = j1-1
        # regresar j
    return i1, j1

def arriba(i1, j1): 
    i=i1 # anterior 
    j=j1 # anterior 
    while a[i1][j1]!=["X"] and i1 >= 0:
        if a[i1-1][j1] == ["X"]:
            return i1, j1
            break
        elif i1==0:
            a[i1][j1]=["A"]
            return i1,j1
        else:
            a[i1][j1]=["A"]
        i1 = i1-1
        # regresar i
        return i1, j1  
    
def buscar(i1, j1):
    if j1==4 and i1<n-1:
        if a[i1+1][j1]!=["X"] and i1<(n):
            direccion= 'abajo'
            return direccion
        elif a[i1][j1-1]!=["X"] and j1>0:
            direccion= 'izquierda'
            return direccion
        elif a[i1-1][j1] != ["X"] and i1>0:
            direccion= 'arriba'
            return direccion
    elif i1==4 and j1<m-1:
        if a[i1][j1+1]!=["X"] and j1<(m):
            direccion = 'derecha'
            return direccion
        elif a[i1-1][j1] != ["X"] and i1>0:
            direccion= 'arriba'
            return direccion
        elif a[i1][j1-1]!=["X"] and j1>0:
            direccion= 'izquierda'
            return direccion
    elif i1==4  and j1 ==4:
        print("")
    else:
        if a[i1][j1+1]!=["X"] and j1<(m):
            direccion = 'derecha'
            return direccion
        elif a[i1+1][j1]!=["X"] and i1<(n):
            direccion= 'abajo'
            return direccion
        elif a[i1][j1-1]!=["X"] and j1>0:
            direccion= 'izquierda'
            return direccion
        elif a[i1-1][j1] != ["X"] and i1>0:
            direccion= 'arriba'
            return direccion

# m,n tamano de la matriz
n = 5
m = 5
# numero de obstaculos 
d = 10
a = [0] * n
# Crear matris 5x5 sin "obstaculos"
for i in range(n):
    a[i] = [0] * m
print(" ")
# agregar obstaculos "x" a la matriz 
for i in range(n):
    for j in range(m):
        x = random.randint(1, d)
        if i==0 and j==0 or i==n-1 and j ==m-1: 
             a[i][j] = ["O"]
        elif x == 1:
            a[i][j] = ["X"]
        else:
            a[i][j] = ["O"]
        
        print(a[i][j], end="")
    print(" ")
print(" ")
# solucion 
i=0
j=0
direccion = 'derecha'
while i!=(n-1) or j!=(m-1):
    direccion = buscar(i,j)
    print(direccion)
    if direccion == 'derecha':
        i, j= derecha(i,j)
        i,j = abajo(i,j)
    elif direccion == 'abajo':
        i, j= abajo(i,j)
        i, j= derecha(i,j)
    elif direccion== 'izquierda':
        i, j= izquierda(i,j)
        i ,j= abajo(i,j)
    elif direccion== 'arriba':
        i, j= arriba(i,j)
        i, j= derecha(i,j)
    print(i,j)
imprimir()
