'''
Se tiene la siguiente lista con DNIs de personas.
    30612453
    23763290
    21448503
    34582048
    15364857
Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.

'''

dni = int(input("Ingrese un numero de DNI: "))

if(dni == 30612453):
    print("Se encuentra en la lista: 30612453")
else:
    if(dni == 23763290):
        print("Se encuentra en la lista: 23763290")
    else:
        if(dni == 21448503):
            print("Se encuentra en la lista: 21448503")
        else:
            if(dni == 34582048):
                print("Se encuentra en la lista: 34582048")
            else:
                if(dni == 15364857):
                    print("Se encuentra en la lista: 15364857")
                else:
                    print("El DNI ingresado no se encuentra en la lista.")

#Este ejercicio ya es un poco mas complejo, ya que requiere un mejor entendimiento de la sentencia if y else, como 
#anidarlos para que segun una respuesta se pregunte otra cosa en base a eso o en su defecto terminar el programa en #alguno de las condiciones. Lo que podemos notar es que realizamos la sentencia else dentro de cada if nuevo que #hacemos, esto se debe a la indentacion, si no esta bien indentado el programa probablemente no haga lo que uno #espera que haga, OJO y atentos a la indentacion, es muy importante, notaras que estan bien anidados los #condicionales cuando las mismas te queden como en cascada tal como se muestra en la resolucion anteriormente #propuesta, y por supuesto entendiendo como se anida un if y un else, es practicar hasta que salga como lo queremos, #jugando un poco con el codigo, sale bastante facil una vez lo haces repetidas veces.