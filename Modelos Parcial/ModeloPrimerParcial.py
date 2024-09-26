'''
Ejercicio 1: (2.5 puntos, 0.5 cada ítem)
a) Si la variable n es un entero y la guarda del if es:
n!= -5 or n > 0 
¿Cuánto debe valer n para que no se cumpla la guarda?
'''

#Respuesta a)
#n es int
#n != -5 o n mayor a 0

#Para que NO se cumpla la guarda, "n" puede tener varios valores
#estos serian, -5 porque la condicion indica que debe ser
#DIFERENTE a -5, es decir, "n" no debe valer -5 antes de
#entrar al ciclo, y por otro lado tenemos otra condicion,
#que "n" sea menor o igual 0, osea todos los numeros negativos
#si en algun momento "n" vale 0 o menos de 0, automaticamente
#el ciclo While termina.

'''
b) Si la variable i vale -2 y la guarda de un condicional es  i<= -2 and i>= -2 ¿Se ejecuta la rama afirmativa o negativa del condicional?
'''

#Respuesta b)
#i = -2
#condicion i menor o igual a -2 Y i mayor o igual a -2

#Se ejecutaria la rama afirmativa, esto debido a que la variable i cumple ambas condiciones al ser menor/mayor IGUAL a -2 osea incluyendo el -2

'''
c) ¿Para qué valores de la variable entera m la siguiente condición es verdadera?:  m <= 3 or m > 2
'''
#Respuesta C)

#La variable "m" deberia valer 3 o enteros menores a 3, o enteros mayores a 2 sin incluir al 2.
'''
d) ¿Qué imprime el siguiente programa?
cadena = “”
for letra in “se viene el frio”:
	if letra != ‘e’:
		cadena = letra + cadena
	else:
		cadena = cadena + letra
print(cadena)
'''
#Respuesta D)

#El programa imprime: "oirf l niv seeee"
'''
e) ¿Cuántas iteraciones realiza el siguiente ciclo?
cont= 11
while (cont> 6):
	print (“Hoy tenemos recuperatorio del Primer Parcial  de IP”)
	cont = cont - 1
'''

#Respuesta E)

#El ciclo hace: 5 iteraciones

'''
Ejercicio 2: (2.5 puntos)
1   print("Perfecto, la suma de los divisores propios es igual al mismo número")
2   n=int(input("ingrese un número"))
3   suma=0
4   for i in range(1, n//(2-1)):
5	if (not n%i):
6       suma=suma+i
7	    print("divisor encontrado: ",i, "suma acumulada: ",suma) 
8   if(suma==n):
9       print(n, "es un número perfecto")
10 else:
11     print(n, “no es un número perfecto”)
'''

'''
a) ¿Qué tipo de variable se encuentra en la línea 3? ¿Para qué se usa?
b) Explique cuál es el rango de valores que tomará el ciclo for (línea 4) 
c) ¿Qué verifica la línea 5 del código? 
d) Resuelva el mismo problema pero utilizando un ciclo while ¿Se requieren nuevas variables? ¿Cuáles?
e) ¿Qué mostraría el programa si n valiera 8? ¿Y si n vale 6?

'''
#Respuesta A)
#En la linea 3 vemos la inicializacion de un acumulador 
#que dentro del ciclo for va acumulando los valores de 
#la variable i en base a si se cumple la condicion de la
#linea 5

#Respuesta B)
#En la linea 5 el rango de valores que tomara el ciclo es
#el resultado de la division n/(2-1) pero redondeando para
#abajo al entero mas cercano dado que es una division con
#doble barra, es decir, segun el usuario ingrese un numero 
#"n" y se divida por (2-1) el resultado de esta operacion 
#sera el rango del ciclo - 1, dado que en el codigo 
#mencionado no se especifica n//(2+1)+1 para incluir el resultado en el rango del ciclo

#Resultado C)
#
