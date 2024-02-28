# Reporte de Practica1 LRT4102
Aldo Fuentes Cruz  167464

**Introducción**
Python es uno de los lenguajes de programación de código abierto mas populares y usados actualmente para desarrollo de software, ciencias de datos y el machine learning (ML), fue desarrollado en 1991, se trata de un lenguaje interpretado, lo que implica que el código generado se convierte en byteocde t se ejecuta por la máquina virtual de Python.

Es un lengujae de alto nivel, puesto que considera las capacidaddes cognitivas del programador, de modo que se vuelve un lenguaje sencillo y fácil de entender, dentro de las características principales de este lenguaje se enecuentran las siguientes:

1) Multiplataforma: es un lenguaje que puede ser empleado en distintos tipos de sistemas operativos, incliyendo Windows, Linux y macOS.
2) Dinámico: las variables pueden tomar valores de diferentes tipos.
3) Multiparadigma: la programción es imperativa, orientada a objetos y funcional.

Los tipos de variables existentes dentro de python respeta las bases de cualquier otro lenguaje, estos son:
- int: crea una variable de tipo integer.
- double: especifica un valor numético con sus decimales.
- char: se emplea para crear una variable que incluye exactamente un carácter.
- string: define una cadena de carácteres en Java.
- bool: representa una variable de valor booleana, es decir, qe toma como valores solo 1 o 0.

  Las principales estructuras de python se basan en las estructuras de C++, con algunas modificaciones en sintaxis pero respetando las bases logicas. Las principales caracteristicas de pthon son la ausencia de punto y coma al final de cada linea, y la relevancia de la indentacion dentro del codigo.    
  Las principales estructuras son:
- if / elif: con "if" y "else" se comprueba si una variable cumple una condición en específico, si la cumple se ejecutará una indicación, en caso de que no se cumpla se realizará la instrucción dictada por "elif".

  El comando completo se emplea de la siguiente forma:

  if (condición):
    [Instrucción si la condición se cumple]
  elif (condición):
    [Instrucción si la condición no se cumple]
  
- for: es una sentencia que genera un bucle con un numero de repeticiones controladas. A diferencia de otros lenguajes de programacion, en python la sentencia for es mas facil y se basa en establecer una variable que ira recorriendo todos los elementos de una lista o arreglo.

  La estructura del comando for es la siguiente:

  for x in range(m,n)
    [Ejecutar instrucción con la variable x tomando cada valor entre m y n]
  
- while: instruccion empleada para generar un bucle indefinido mientras la condición definida se verdadera.

  Su estructura correspondiente es la siguiente:

  while (condición de termino)
    [Ejecutar instrucción hasta que la condición sea válida]

**Problemas a resolver**

**1) Escribir un programa que lea un entero positivo “n” introducido por el usuario y después muestreen pantalla la suma de todos los enteros desde 1 hasta n . La suma de los primeros enterospositivos puede ser calculada de la siguiente forma.**

Para dar solucion a este problema, se usa una formula conocida para la suma de numeros consecutivos desde 0 hasta n.
Por lo que lo unico que se necsita como entrada es el valor de n en la ecuacion. 
  #Se solicita al usuario el valor de n en la ecuación dada
  n = int(input("Introduzca el valor de n "))

  #Se realiza la operación
  suma = n*(n+1)/2

  #Se imprime el resultado
  print("el valor de la operación es", suma)
  
   
**2) Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después debe mostrar por pantalla la paga que le corresponde.**
 
La logica usada para resolver este problema es muy simple, como datos de entrada son necesarios dos datos, las horas trabajadas, y el salario o costo, una vez dados esos datos, el resultado corresponde a la multiplicacion

        #Se solicita al usuario el número de horas trabajadas, así como el costp (salario) por horas.
        horas = float(input("Horas trabajadas "))
        
        horas = float(input("Las horas trabajadas por el empleado son: "))
        
        costo = float(input("El costo por hora del empleado es: "))
        
        total = horas * costo
        
        print("El costo del empleado es: ", total)
  
   
**3) Crea una lista de nombre + sueldo por hora + horas trabajadas de al menos seis operadores. Imprime el nombre y el sueldo a pagar de cada operador.**

Para la solución de este problema se necesita usar listas, en donde se ingresaran los datos. Lo primero que se necesita saber es la cantidad de elementos que tendrá cada lista, por lo que el primer paso es solicitar al usuario el numero de empleados, una vez dado este valor se crear 4 llistas vacías donde se almacenaran los datos, una lista para nombre, otra para horas, otra para salario y una cuarta lista que contendrá toda la información anterior. 
Para ingresar los datos requeridos a las listas se usa un for que ira desde el 0 hasta el numero ingresado por el usuario en el paso anterior. Dentro del for se pide al usuario que ingrese los datos del trabajar, el nombre, pago por hora y las horas trabajadas, una vez que el usuario ingreso los datos se agregan a las listas correspondientes con la función lista.append(dato). En este punto ya se deben encontrar llenas todas las listas con los datos correspondientes para los n trabajadores, el ultimo paso es ordenar todos los datos en una lista que contenga toda la información de todos los trabajadores. Para esto se usa otro ciclo for hasta el numero n. la estructura de la nueva lista es: 
Nombre Trabajador 1   $ (salario trabajador 1)
Nombre Trabajador 2 $ (salario trabajador 1)
        ………………………………………
Nombre Trabajador n $ (salario trabajador n)

Por último, se imprime la lista completa en la terminal. 


        #Se solicita el núero de empleados
        n = int(input("Numero de empleados "))

        #Se crean 3 listas, unoa para cada variable que se empleará, así como 1 extra para la lista final de nombre y sueldo
        
        list_nombres = []
        
        list_horas = []
        
        list_salario = []
        
        Lista = []

        #Se crea un for que se repetirá las mismas veces que el tamaño del vectores
        
        #Se solicitan el nombre, costo y horas trabajadas de cada empleado
        
            for i in range(n):
        
            nombre = str(input("Ingrese el nombre del empleado: "))
            
            costo = float(input("Ingrese el costo por hora del empelado: "))
            
            horas = float(input("Ingrese las horas trabajadas por el empelado: "))
            
            
            #Se realiza la operación y se guardan en cada una de las listas creadas
            
            total = horas * costo
            
            list_nombres.append(nombre)
            
            list_horas.append(horas)
            
            list_salario.append(total)
        
        #Se imprimen los resultados de cada empleado
        
        for i in range(n):
        
            Lista.append(list_nombres[i] + "  $" + str(list_salario[i]))
            
        print(Lista)
  

 


**4) Crea una lista llamada numeros que contenga al menos 10 números. Calcula el promedio de los números pares y el producto de los números impares. Imprime los resultados.**

Para resolver este problema se necesita solo un valor de entrada, en base al cual re realizaran las operaciones solicitadas. Por lo tanto, el primer paso es pedir al usuario que ingrese un numero que sea mayor a 1. Luego se debe generar un rango de valores entre 1 y el numero que ingreso el usuario, dicho rango será usado en las iteraciones del tipo for. El siguiente paso es definir las variables y crear las listas vacías que serán usadas, se necesitarán 2 listas una para números pares (numP) y otra para números impares (numI), una variable con valor inicial cero donde se guardara la suma de los números pares (sumaP), y por último una variable donde se guardara el producto de los impares con valor inicial iguala a 1 (producto).  El siguiente paso consiste en separar los pares de los impares, para realizar esto se usa una iteración for desde el 1 hasta el numero ingresado por el usuario, dentro de esta iteración a cada valor se le aplica el operador modulo para determinar si es un numero par, si lo es se agrega a la lista de números pares (numP.append(i)) y se suma este número a la variable sumaP. Si no es par, entonces es impar y se agrega a la lista de impares (numI.append(i)) y se multiplica por la variable producto y se actualiza con este nuevo valor. Al final de la iteración la lista de números pares y la lista de impares ha sido llenada correctamente. El siguiente paso consiste en imprimir la lista de los números pares para que el usuario pueda ver la operación que se realizó y como se hizo, para imprimir los números pares en una sola línea dentro de la terminal se usa la instrucción end=’’ dentro de print, de esta forma se pueden imprimir los elementos de las listas sin tener un salto de línea. Por ultimo se calcula el promedio de los pares mediante la división de la variable sumaP entre la longitud de la lista numP. Y se imprimen los resultados. 

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

**5) Crea un programa que solicite al usuario adivinar un número secreto. El programa debe generarun número aleatorio entre 1 y 10, y el usuario debe intentar adivinarlo. El programa debe proporcionar pistas si el número ingresado por el usuario es demasiado alto o bajo. El bucle while debe continuar hasta que el usuario adivine correctamente. Al final se debe imprimir en cuantos intentos el usuario logró adivinar el número.**


Para este problema se requiere crear una variable que contenga un numero aleatorio entre 1 y 10, para lograrlo se usa la función random incluida dentro de la librería random, por lo que para hacer uso de esta función es necesario importar dicha librería. El programa empieza por la creación del numero aleatorio y pide al usuario que intente adivinar el numero ingresando un número. El siguiente paso consiste en un bucle indefinido de tipo while, que se estará repitiendo hasta que el dato ingresado por el usuario se igual que el numero generado aleatoriamente. Dentro del bucle while, primero se calcula la diferencia entre el numero aleatorio y el ingresado por el usuario, si dicha diferencia es mayor que cero significa que el usuario ingreso un numero menor al generado aleatoriamente por lo que se le dará la pista al usuario de que el numero debe ser mayor, de lo contrario se le dará el mensaje de que el numero deberá ser menor y se le pedirá al usuario ingresar un número.  Por ultimo cuando la condición del bucle while no se cumpla se procederá a imprimir el mensaje “Lo has logrado”. 

            import random
            #generar numero aletario entre 1 y 10
            numero_secreto = random.randint(1, 10) 
            print("El sistema ha generado un numero secreto intenta adivinarlo")
            a = int(input(" Ingresa el numero :" )) 
            while (a!= numero_secreto):
                dif = numero_secreto - a
                print("numero Incorrecto ", end="")
                if dif > 0:
                    print(" debe ser un valor mayor")
                else:
                    print("debe ser una valor menor")
                a = int(input("ingresa otro numero :"))
            print(" Lo has logrado el numero aleatorio era ", a)
   

**6) Robot explorador: El programa debe generar una matriz de al menos 5x5. El robot inicia su camino en la posición (0,0) de la matriz y debe salir en la posición (4,4) o la máxima posición si se cambia el tamaño de matriz. El numero y la posición de los obstáculos es aleatoria. El robot solo puede avanzar, girar a la izquierda o a la derecha para buscar un camino libre, en el eventual caso que el robot no pueda salir debe imprimir en pantalla “Imposible llegar al destino”. En caso de que el robot llegue a su destino final deberá imprimir el mapa, con los espacios libres yobstáculos de la siguiente forma:
X obstáculo o libre.**


Para resolver este problema el primer paso es definir el tamaño de la matriz definiendo los valores de las variables m y n. que están establecidas en le programa como 5 y 5. Después se crea una matriz de tamaño m x n de puros ceros. El siguiente paso es agregar obstáculos a la matriz que son representados con un X, para realizar esto se usa un ciclo for y mediante un numero aleatorio se determina la posición de los obstáculos, es importante que el inicio de la matriz (0,0) y el final (4,4) siempre deben estar libres, es decir tener una O. Una vez establecida la matriz se procede a la solución, como primer paso se establecen las variables i y j con las coordenadas de inicio, en este caso (0,0), después en un bucle while se procede a usar la funcion buscar la cual fue creada para resolver este problema, y dependiendo de el valor devuelto por la función buscar se procede a ejecutar el movimiento correspondiente, que también son funciones definidas. 
  

            import random
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


funcion buscar 


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

funciones de direccion 

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

funcion para imprimir la matriz 
    def imprimir():
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print(" ")