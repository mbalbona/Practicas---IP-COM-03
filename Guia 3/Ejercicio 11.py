'''
Ejercicio 11

a) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla todos los divisores de n.
b) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla todos los divisores pares de n.
c) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla la cantidad de divisores de n.
d) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla la suma de los divisores de n.
e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
muestre en pantalla los primeros c divisores de n.
f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
muestre en pantalla los últimos c divisores de n.

'''
#A)
""" n = int(input("Ingrese un numero: "))

for i in range(1, n+1, 1):
    if(n%i == 0):
        print(i, " ")
 """        
#B)

""" n = int(input("Ingrese un numero: "))

for i in range(1, n+1, 1):
    if(i%2 == 0):
        if(n%i == 0):
            print(i, " ")
 """
#C)

""" n = int(input("Ingrese un numero: "))
cont = 0

for i in range(1, n+1, 1):
    if(n%i == 0):
        cont+=1
        
print("La cantidad de divisores de", n,"son: ", cont) """

#D)

""" n = int(input("Ingrese un numero: "))
acum = 0

for i in range(1, n+1, 1):
    if(n%i == 0):
        acum += i
        
print("La suma de los divisores de", n,"son: ", acum) """

#E)
""" n = int(input("Ingrese un numero: "))
c = int(input("Ingrese un segundo numero: "))

cont = 0

for i in range(1, n+1, 1):
    if(n%i == 0):
        print(i, " ")
        cont+=1
        if(cont >= c):
            break """
        
#F)
n = int(input("Ingrese un numero: "))
c = int(input("Ingrese un segundo numero: "))
i = 1
cont = 0
ultimo_divisor = 0

while i <= n:
    if n % i == 0:
        cont += 1
        ultimo_divisor = i
        
        if(cont > c):
            print(ultimo_divisor, end=" ")

    i += 1
