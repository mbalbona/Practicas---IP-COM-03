'''
Escribir un programa que solicite al usuario un número positivo y aproxime el valor del número
e de la siguiente manera: (ejemplo para 7 términos)

1/0! + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! + 1/6!

'''
#ingreso
n = int(input("Ingrese el numero a aproximar: "))

#Declaracion de variables
result = 0
factorial = 1

#Se hace un for para el n ingresado por el usr
for i in range (1, n+1):
    #Se hace un segundo for donde calculamos el factorial y lo asignamos a la variable
    for j in range(i,i+1,1):
        factorial *= i
    
    result += 1/factorial
    
    #Volvemos a poner la variable en 1 para que vuelva a realizar el calculo de factorial desde 1 hasta la vuelta que este dando el primer ciclo for declarado
    factorial = 1        

print("El resultado de la aproximacion es: ", result)