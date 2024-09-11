'''
Ejercicio 15
a) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir,
2 6 12 20...
b) Idem anterior para la sucesión an = n^2.
c) Idem anterior para la sucesión an = n^3 - n^2.
d) Idem anterior para la sucesión an = 1/n^2 .
e) ¿A qué valor se va acercando la suma del inciso anterior a medida que utilizamos un valor alto de n?
'''
n = int(input("Ingrese un numero: "))
acum = 0

#A)

for i in range(1, n+1):
    acum += 2
    print(acum, end=" ")


#B)
 
for i in range (1, n+1):
    acum += i**2
    print(acum, end=" ") 
    
#C)

for i in range (1, n+1):
    acum += (i**3 + i**2)
    print(acum, end=" ") 

#D)

for i in range (1, n+1):
    acum += (1/(i**2))
    print(acum, end=" ")
    
#E)

#El valor al que mas se acerca le inciso anterior es al numero 2.0 a medida que vamos aumentando el N