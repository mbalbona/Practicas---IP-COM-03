'''
Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
"Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.
'''

n1 = float(input("Ingrese el primer numero flotante: "))
n2 = float(input("Ingrese el segundo numero flotante: "))

promedio = (n1 + n2) / 2

if(promedio > 7):
    print("Aprobado")
else:
    print("Desaprobado")
    
#Este ejercicio es similar a los anteriores con un condicional, la diferencia es que ahora estamos combinando
#la condiciones con operaciones matematicas, el resultado de esa operacion la almacenamos en una variable auxiliar y #en base a eso hacer preguntas con esa variable auxiliar como nexo para sacar el resultado que nos pide el #ejercicio, que en este caso seria segun un promedio (suma de todas las notas, dividido la cantidad de notas que #hay, este caso son 2 y lo ponemos manualmente, en un futuro no lo haremos manualmente para calcular este tipo de #situaciones) saber si un alumno esta aprobado o desaprobado.