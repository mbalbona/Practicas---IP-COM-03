'''
Ejercicio 9 

Hacer un programa que solicite un número x, en caso de ser par realiza x/2 y en caso contrario
3x + 1 y repite el procedimiento hasta obtener el número 1. El programa debe indicar cuantas
veces se tuvo que repetir el procedimiento. Por ejemplo, si se ingresa el número 10 el programa
devuelve 6, porque 10 es par entonces lo divide por 2 y da 5, como es impar lo multiplica por 3 y
le suma 1 obteniendo 16. Luego da 8, 4, 2 y 1. Otro ejemplo: si se ingresa 27 debe devolver 111

'''

x = int(input("ingrese un numero: "))

cont = 0

if(x % 2 == 0):
    x = x / 2
else:
    x = 3 * x + 1
    
cont+=1

while x != 1:
    if(x % 2 == 0):
        x = x / 2
    else:
        x = 3 * x + 1
    cont+=1

print("Este proceso se realizo: ", cont, " veces")