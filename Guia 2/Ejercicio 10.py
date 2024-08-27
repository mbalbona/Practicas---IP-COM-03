'''
Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
caja de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
comienzo y al fin del período.
'''

kw_consumidos = float(input("Ingresar cantidad de kw consumidos: "))

importe = float(480) #Valor base de los primeros 200kw consumidos en float debido a que puede ser decimal el importe
aux = 0 #Declaramos una variable auxiliar a 0 para poder calcular el excedente 

if(kw_consumidos <= 200):
    importe += 78                       #Si no excede unicamente se le suma el impuesto
else:
    if(kw_consumidos > 200):
        aux = kw_consumidos - 200       #sacamos la diferencia para saber cuantos kw tenemos de excedente
        
        importe += (aux * 25.5) + 78    #Multiplicamos por 25,5 que es lo que indica que esta el kw excedido de 200
                                        #y sumamos el impuesto
                             
print("El importe total es de: ", importe, "pesos")


    
    

