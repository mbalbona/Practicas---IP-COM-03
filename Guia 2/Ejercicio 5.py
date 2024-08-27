'''
Escribir en papel un programa que pida una nota y que en el caso de que sea menor a cuatro
muestre "Debe recuperar". Luego pasarlo a Python.
'''
nota = int(input("Ingrese una nota: "))

if(nota < 4):
    print("Debe recuperar")
    
#Este programa como vemos es bastante sencillo.
#Unicamente pediremos al usuario que ingrese un numero que tomaremos como una nota
#luego con un condicional if preguntaremos si el valor almacenado en la variable "nota" es
#menor a 4 el cual utilizaremos el simbolo matematico de las boquitas, tanto para menor como para mayor
#(< y >), con las boquitas unicamente estamos preguntando si determinada variable o determinado numero es mayor a
#tal otro, pero sin incluir dicho numero, es decir, si tenemos una nota 4 y nuestro enunciado dice que debe recuperar
#con nota menor o igual a 4 y utilizamos la boquita de menor (<), este no incluiria el 4 y por ende el ejercicio 
#estaria mal, en estos casos que deseamos incluir el numero sobre el cual estamos haciendo la condicion, debemos usar
#las boquitas seguidas del signo igual, por ejemplo en el ejemplo anterior, deberiamos usar: nota <= 4, lo mismo
#si deseamos que sea mayor incluyendo el numero sobre el que estamos haciendo la condicion, seria, nota >= 4

#en resumen: Sin incluir el numero boquitas solas (< y >)
#            incluyendo el numero: boquitas seguidas de un igual (<= y >=)