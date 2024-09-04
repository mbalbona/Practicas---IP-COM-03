'''
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
7 (4, 5, 6 y 7).
b) Hacer un programa que permita al usuario elegir un número m y un n y luego
muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n - 1, n). ¾Qué pasa
si n es menor que m?
'''

#A)

for i in range(4,8, 1):
    print(i)
    
#B)


n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

for i in range(n1, n2+1, 1):
    print(i)
    