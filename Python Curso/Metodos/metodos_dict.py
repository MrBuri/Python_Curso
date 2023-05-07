diccionario = {
    "nombre" : "Buri",
    "apellido" : "WTF",
    "fans" : 0
}

#Nos delvuelve un objeto dict_item 
claves =diccionario.keys()


#Obteniendo un elemento con (get)(no lanza una excepcion y si no encuentra nada el programa continua)
valor_de_JAJA =diccionario.get("JAJA")
print("El programa continua")

#Eliminando todo del diccionario 
#diccionario.clear()

#Eliminando un elementodel diccionario  
diccionario.pop("apellido")

#obteniendo un elemento  dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)