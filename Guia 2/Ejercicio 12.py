'''
Un profesor clasifica las notas de sus alumnos de la siguiente manera:
    1-3 Reprobado
    4-6 Debe rendir examen final
    7-10 Eximido
    
a) Escribir un programa que indique la clasifcación de una nota.
b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
del mismo.
'''

#nota = int(input("Ingrese la nota a analizar: "))

#A)
'''
if((nota >= 1) and (nota <= 3)):
    print("Reprobado")
else:
    if((nota >= 4) and (nota <= 6)):
        print("Debe rendi examen final")
    else:
        if((nota >= 7) and (nota <= 10)):
            print("Eximido")
'''         
#B)

nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if((promedio >= 1) and (promedio <= 3)):
    print("Reprobado")
else:
    if((promedio >= 4) and (promedio <= 6)):
        print("Debe rendi examen final")
    else:
        if((promedio >= 7) and (promedio <= 10)):
            print("Eximido")
