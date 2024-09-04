'''
a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
(1, 2, 3, 4 y 5).
b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
primeros n números naturales (1, 2, · · · , n)
'''

#A)
for i in range(1,6,1):
    print(i)

#B)    
n = int(input("Ingrese un numero: "))

for i in range(1, n+1, 1): #n+1 para incluir el numero ingresado dado que si ponemos n, no va a incluirlo
    print(i)