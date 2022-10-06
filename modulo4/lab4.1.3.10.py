'''
Descripcion:Convirtiendo el consumo de combustible
Autor: Isidro Lara López
Fecha: 4 octubre 2022
'''
#def liters_100km_to_miles_gallon(liters):
 #gallon = liters / 3.785411784
 #millas = 100 * 1000 / 1609.344
 #return millas / gallon
    

#def miles_gallon_to_liters_100km(miles):

 #km100 = miles * 1609.344 / 1000 / 100
#litros = 3.785411784
#return litros / 100


#print(liters_100km_to_miles_gallon(3.9))
#print(liters_100km_to_miles_gallon(7.5))
#print(liters_100km_to_miles_gallon(10.))
#print(miles_gallon_to_liters_100km(60.3))
#print(miles_gallon_to_liters_100km(31.4))
##print(miles_gallon_to_liters_100km(23.5))
def liters_100km_to_milles_gallon(litros):
    galones = litros / 3.785411784
    milles = 100 * 1000 / 1609.344
    return milles / miles_gallon_to_liters_100km
    
def miles_gallon_to_liters_100km(milles):
    km100 = milles * 1609.344 / 1000 / 100
    litros = 3.785411784
    return litros / km100


print(liters_100km_to_milles_gallon(3.9))
print(liters_100km_to_milles_gallon(7.5))
print(liters_100km_to_milles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))