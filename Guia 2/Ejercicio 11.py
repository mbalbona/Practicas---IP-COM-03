'''
Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
verificar los resutlados.
'''

n1 = int(input("Ingresar el primer numero: "))
n2 = int(input("Ingresar el segundo numero: "))
n3 = int(input("Ingresar el tercer numero: "))

num_mayor = 0

if((n1 > n2) and (n1 > n3)):
    num_mayor = n1
else:
    if((n2 > n1) and (n2 > n3)):
        num_mayor = n2
    else:
        if((n3 > n1) and (n3 > n2)):
            num_mayor = n3
        else:
            if(num_mayor == 0):
                print("Todos los numeros son iguales")
            
print("El numero mas grande es: ", num_mayor)


