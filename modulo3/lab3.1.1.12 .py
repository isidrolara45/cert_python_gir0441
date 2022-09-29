
'''
Descripcion: Fundamentos de la sentencia if-elif-else
Autor: Isidro Lara López
Fecha: 27 sep 2022
'''

year = int(input("Introduce un año:"))
if year % 4 != 0: # No es divisible entre 4
    print( 'Año Comun')
    
elif  year % 100 !=0: # Año Bisiesto
    print("Año bisiesto")
elif year % 400 !=0:
    print('Año Comun')
else:
    print(" Año Bisiesto")

    
