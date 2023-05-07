#creando una lista con list
lista = list([23])

#Devuelve la cantidad de elementos de la lista 
cantidad_de_elementos= len(lista)

print(cantidad_de_elementos)

#Agregando un elemento a la lista
lista.append(56)
print(lista)

#Agregando un elemento a la lista con un indice espefico 
lista.insert(2,45)
print(lista)

#agregando varios elementos a la lista
lista.extend([67, 2023])
print(lista)

#eliminando un elemento de la lista (por su indice) (-1 elimina el ultimo y asi sucesivamente)
lista.pop(0)
print(lista)

#removiendo un elemento de la lista por su valor 
#lista.remove("Hola")
print(lista)

#Eliminando todo los elementos de la lista
#lista.clear()
print(lista)

#ordenando la lista de forma ascendete (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()
print(lista)

#Invirtiendo los elementos de una lista 
lista.reverse()
print(lista)

#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(56)
print(elemento_encontrado)





