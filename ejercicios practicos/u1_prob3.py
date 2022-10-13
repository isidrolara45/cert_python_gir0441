dinero = 0 
impuesto = 0
dinero = float(input('Ingresa la catidad: '))
if dinero > 0 and dinero < 10000: 
    impuesto =dinero * 0.05
    print("El impuesto es: ",impuesto) 
elif dinero > 10000 and dinero < 20000: 
    impuesto=dinero* 0.15
    print("El impuesto es: ",impuesto) 
elif dinero > 20000 and dinero < 35000: 
    impuesto =dinero * 0.20
    print("El impuesto es: ",impuesto) 
elif dinero > 35000 and dinero < 60000: 
    impuesto= dinero * 0.30
    print("El impuesto es: ",impuesto) 
else: 
    impuesto=dinero * 0.45
    print("El impuesto es: ",impuesto) 