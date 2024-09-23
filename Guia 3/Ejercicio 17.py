'''
El numero 1/4π se puede aproximar de la siguiente manera:

1/4π = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15

a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
que muestre la aproximación de π con esa cantidad de términos.

b) A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que da la calculadora?

c) A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que da la calculadora?

d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,pida al usuario un número decimal e (muy chico) y calcule la suma hasta que el error comparado con el valor de la calculadora sea menor que e

'''

#A)

n = int(input("Ingrese la cantidad de terminos a sumar: "))

aprox = 0
signo = 1
cont = 1

for i in range (1, n+1,1):
    aprox = aprox + 1/cont * signo
    signo *= -1
    cont += 2
    
print ("La aproximacion de π es:", aprox)