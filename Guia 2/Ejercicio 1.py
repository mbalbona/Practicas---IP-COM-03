'''
Este programa chequea una serie de condiciones para los tres valores ingresados por el usuario.
Correrlo tal cual está en Python. Luego reemplazar donde dice True por una expresión lógica
que sea True o False según corresponda, en lugar de siempre True como ahora.

a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))
print("Usted ingresó los valores:", a, b, c)
print(a, "es mayor que", b, True)
print(a, "y", b, "son iguales", True)
print(a, "es el mayor de todos", True)
print(b, "es el menor de todos", True)
print(a, "es mayor que alguno de los otros dos", True)
print(a, "es menor o igual que alguno de los otros dos", True)
print("Los tres numeros son iguales", True)
print("Los tres numeros son distintos", True)
print(a, "es par", True)
print("alguno es par", True)
print("ninguno es par", True)
print("todos son pares", True)
print(a, "es multiplo de 3", True)
print(a, "es multiplo de 3 y de 5", True)
print(a, "es multiplo de 3 y par", True)
print(a, "-", b, "da un numero positivo", True)
print(a, "-", b, "da un numero par positivo", True)
'''

#Podemos realizar un comentario de multiples lineas con 3 comillas simples al inicio y 3 al final como se indica en
#en el comentario multiple de la linea 1 a la 26. 
#Para los comentarios de una sola linea se usa el numeral (#)

#Resolucion de ejercicio 1
a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))
print("Usted ingresó los valores:", a, b, c)
print(a, "es mayor que", b, False)
print(a, "y", b, "son iguales", False)
print(a, "es el mayor de todos", False)
print(b, "es el menor de todos", False)
print(a, "es mayor que alguno de los otros dos", False)
print(a, "es menor o igual que alguno de los otros dos", True)
print("Los tres numeros son iguales", False)
print("Los tres numeros son distintos", True)
print(a, "es par", True)
print("alguno es par", True)
print("ninguno es par", False)
print("todos son pares", True)
print(a, "es multiplo de 3", False)
print(a, "es multiplo de 3 y de 5", False)
print(a, "es multiplo de 3 y par", False)
print(a, "-", b, "da un numero positivo", False)
print(a, "-", b, "da un numero par positivo", False)

#Nosotros ingresamos la secuencia de numeros: 10, 20, 30 y adaptamos el ejercicio segun se indica
#Siguiendo las condiciones que plantea el ejercicio con los numeros ingresados.
#Modificamos manualmente las sentencias que estaban en true segun la secuencia 10,20,30 eran verdadera o falsa en
#cada linea print().