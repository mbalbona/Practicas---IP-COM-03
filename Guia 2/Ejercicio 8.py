'''
Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
y muestre por pantalla "Usted ingresó un número de una sola cifra" o "Usted ingresó un número
de más de una cifra" según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
y luego correrlo en la computadora con los valores iniciales de las corridas y verificar que hayan
dado como se esperaba.
'''

#Entrada de datos
n1 = int(input("Ingrese un numero: "))

if(n1 > 0 and n1 < 10):
    print("Usted ingresó un número de una sola cifra")
else:
    if(n1 > 9):
        print("Usted ingresó un número de más de una cifra")
