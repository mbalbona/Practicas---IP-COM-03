'''
Ejercicio 16 F
El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:

ln(2) = 1 - 1/2 + 1/3 + 1/4 + 1/5 ...

a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
que muestre la aproximación de ln(2) con esa cantidad de términos.
b) ¾A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
da la calculadora? En python se puede aproximar este valor usando math.log(2)
c) ¾A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
da la calculadora?
d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
pida al usuario un número decimal e (muy chico) y calcule la suma hasta que el
error comparado con el valor de la calculadora sea menor que e
'''
import math

n = int(input("Ingrese la cantidad de terminos a sumar: "))
aprox = 0

#A)
for i in range(1,n+1):
    if i%2 == 0:
        aprox -= 1/i
    else:
        aprox += 1/i

print("Aproximacion de ln(2):", aprox)    

