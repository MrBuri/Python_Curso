#creando diccionarios con dict()

diccionario = dict(nombre="BUri",apellido="WTF")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos 
diccionario={frozenset(["BUri","EL diavlo"]):"JAJA"}

#creando diccionarios con fromkeys() valor por defecto. None
diccionario=dict.fromkeys(["nombre","apellido","Familia"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "NO se"
diccionario=dict.fromkeys(["nombre","apellido"],"NO se")


print(diccionario)