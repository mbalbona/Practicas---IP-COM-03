'''
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
11 salteando de a 2 elementos (5, 7, 9 y 11)
b) Hacer un programa que permita al usuario elegir un número m y un n y luego
muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
2, 5, 8, 11, 14.
c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
el programa deberá mostrar 2, 6, 10, 14.

'''
#A)

for i in range(5, 11+1, 2):
    print(i, end="-")
    
#B)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

for i in range(num1, num2+1, 3):
    print(i, end="-")
    
#C)

num1 = int(input("\nIngrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

for i in range(num1, num2+1, num3):
    print(i, end="-")