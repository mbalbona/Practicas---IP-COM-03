'''
Ejercicio 13
Hacer un programa que reciba un número m y determine el primer n para el cual la suma
1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11

'''

n = int(input("Ingrese un numero: "))
acum = 0
cont = 0
#Con un FOR
for i in range(1, n+1):
    acum += i
    if(acum > n):
        print("El numero es: ",i)
        break

#Con un While
while acum < n:
    cont+=1
    acum += cont

print("El numero es: ", cont)