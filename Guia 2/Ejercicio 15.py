'''
Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
b el intermedio y en c el mayor (es decir, ordenará los valores).
'''

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

aux = 0

if (a > b):
    aux = b
    b = a
    a = aux
if (a > c):
    aux = c
    c = a
    a = aux
if (b > c):
    aux = c
    c = b
    b = aux
    
print("Los numeros ordenador son: ", a, b, c)


