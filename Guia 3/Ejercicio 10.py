'''
Ejercicio 10

a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.
b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
16 32.
c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
256.


'''

#A)

n = int(input("Ingrese un numero: "))

for i in range(0, n+1, 1):
    if(2**i < n):
        print(2**i)

#B)

n = int(input("Ingrese un numero: "))
cont = 0
iterador = bool(1)
    
while iterador == 1:
    if(n <= 0):
        n = int(input("Numero ingresado incorrecto, ingrese nuevamente un numero valido: "))
    else:
        if(cont < n):
            print(2**cont)
            cont+=1
        else:
            iterador = 0 
            
#C)
    
n = int(input("Ingrese un numero: "))
cont = 1
iterador = bool(1)
    
while iterador == 1:
    if(n <= 0):
        n = int(input("Numero ingresado incorrecto, ingrese nuevamente un numero valido: "))
    else:
        if(cont <= n):
            print(cont**cont)
            cont+=1
        else:
            iterador = 0