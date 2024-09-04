'''
a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
siguen al 10 (11, 12, · · · , 15).
b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
c) Hacer un programa que permita al usuario elegir un número n y un número c, y
luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).
'''

#A)
n = 10
for i in range(n+1, n+6, 1):
    print(i)
    
#B)
n = int(input("ingrese un numero: "))
for i in range(n, n+6,1):
    print(i)

#C)
n = int(input("ingrese un numero: "))
c = int(input("ingrese cuantos numeros que le siguen quiere mostrar: "))

for i in range(n, n+(c+1),1):
    print(i)