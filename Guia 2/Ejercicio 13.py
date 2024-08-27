'''
Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
mayor que el segundo o viceversa.
'''

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if(n1 > n2):
    print("El primer numero es mayor al segundo")
else:
    if(n2 > n1):
        print("El segundo numero es mayor al primero")
    else:
        if(n1 == n2):
            print("Ambos numeros son iguales")
            