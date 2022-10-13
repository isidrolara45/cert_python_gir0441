'''
Nombre: Isidro Lara López
Fecha:  26 / sep /2022
Descripción:Programa para saber si el año que introdujistes es bisiesto o no. 
'''
year = int(input("Introduce un año: "))
if(year <= 1582): 
    print('No esta dentro del período del calendario Gregoriano')
elif year % 4 !=0: 
    print('Año Común') 
elif year % 100 !=0: 
    print('Año Bisiesto')
elif year % 400 !=0:
    print('Año Común') 
else: 
    print('Año Bisiesto')