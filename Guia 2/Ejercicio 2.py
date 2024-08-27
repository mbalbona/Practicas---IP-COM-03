'''
Un ciudadano argentino está exento de votar en estos casos:
- Tiene más de 70 años
- Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.

Suponiendo que las variables edad y distancia representan la edad y la distancia del ciudadano, escribir la expresión lógica que representa esta situación.
'''

edad = int(input("Ingrese la edad: "))
distancia_ciudadano = int(input("Ingrese la distncia a la que se encuentra: "))

if(edad <= 18):
    print("Es menor de edad, no debe votar")
else:
    if((edad > 18) and (edad < 70)):
        if(distancia_ciudadano > 500):
            print("Exento")
    else:
        if(edad > 70):
            print("Exento")
        else:
            if((edad > 18) and (distancia_ciudadano < 500)):
                print("tiene que votar")
        
#Este ejercicio lo llevamos un poco mas alla de lo que se pide inicialmente, nada super rebuscado.
#unicamente se agregan las expresiones logicas and y or (Leer pagina 3 de la practica 2).
#Jugamos un poco con lo que pide el ejercicio y hacemos que nos imprima en pantalla si esta extento de votar o no.
#Primero hacemos la carga de datos: edad y distancia segun indica el enunciado, inicialmente debemos saber
#con que datos trabajamos, si seguimos el enunciado nos podemos dar cuenta que dice "suponiendo" que las variables
#sean edad y distancia(le agregue un dato mas al nombre de la variable, no afecta el funcionamiento) tenemos que }
#hacer un programa que tenga las condiciones para que un ciudadano argentino este exento de votar, las condiciones
#dadas al inicio del enunciado. En caso de tener una mejor idea o mejor resolucion indicarmelo y lo vemos.