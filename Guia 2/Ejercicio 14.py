'''
Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
valores de las variables y mostrarlos de mayor a menor.

'''
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

aux = 0

if(n1 < n2):
    aux = n1
    n1 = n2
    n1 = aux 
    
if(n1 > n2):
        print(n1, " ", n2)
else:
    if(n2 > n1):
        print(n2, " ",n1)
        
#No especifica que salida tiene el programa en caso de que el primer numero sea mayor al segundo
#asumimos que siempre la salida es los numeros de mayor a menor
