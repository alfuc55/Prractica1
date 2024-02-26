n = int(input("Numero de empleados "))
list_nombres = []
list_horas = []
list_salario = []
Lista = []
for i in range(n):
    nombre = str(input(" ingresa nombre "))
    costo = float(input("costo por hora "))
    horas = float(input("Horas trabajadas "))
    total = horas * costo
    list_nombres.append(nombre)
    list_horas.append(horas)
    list_salario.append(total)
for i in range(n):
    Lista.append(list_nombres[i] + "  $" + str(list_salario[i]))
print(Lista)


