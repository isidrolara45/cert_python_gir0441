'''
Descripcion:   Variables, un sencillo convertidor
Nombre:Isidro Lara López
Fecha: 22 sep 2022
'''

kilometers = 12.25
miles = 7.38
'''
   1 milla = 1.61 kilometros
   738 millas =?   = 12.25 kil
   '''

miles_to_kilometers = miles * 1.61 / 1
kilometers_to_miles = kilometers *1 / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
