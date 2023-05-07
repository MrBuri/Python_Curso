Ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else if (elif)

if Ingreso_mensual > 10000:
    if Ingreso_mensual - gasto_mensual < 0:
        print("Estas En la Quiebra bro._.")
    elif Ingreso_mensual - gasto_mensual > 3000:
        print("Vamo Bien Broder")
    else:
        print("Estas gastando Mucho en las cariñosas")
       
elif Ingreso_mensual > 1000:
    print("Estas bien en latam")
    
elif Ingreso_mensual > 500:
    print("Estas bien en Colombia")

elif Ingreso_mensual > 200:
    print("Estas bien en Venezuela")

#Si todas las anteriores no se cumplen(else)
else:
    print("Pobre :c")