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