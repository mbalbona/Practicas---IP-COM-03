'''
Ejercicio 14
a) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
6...
b) Idem anterior para la sucesión an = 2n - 1.
c) Idem anterior para la sucesión an = n
2
.
d) Idem anterior para la sucesión an = n
3 - n
2
.
e) Idem anterior para la sucesión an =
1
n2 .
'''

n = int(input("ingrese un numero: "))

#A)

for i in range(1, n+1):
    print(2 * i, end=" ") 
    
#B)

for i in range(1, n+1):
    print((2*i) - 1, end=" ") 
    
#C)

for i in range(1, n+1):
    print(i**2, end=" ") 
    
#D)

for i in range(1, n+1):
    print ((i**3) - (i**2), end=" ")
    
#E)

for i in range (1, n+1):
    print (1/(i**2), end=" ")