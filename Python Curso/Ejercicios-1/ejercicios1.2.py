#Le pedimos al usuario que nos indique una frase (O Varias)
frase = input("decime una frase y te calculo cuando tardarias si tuvieras que decirla: ")

#Creamos una lista con todas las palbras de la frase (Las separa cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto en decirlo. le indicamos que se calme
if cantidad_de_palabras > 120:
    print("Calma, Mucho texto kpo")    

#Calculamos cuando tardaria en decir la palabra, y se lo Indicamos
print(f"DIjiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"La maquina lo diria en {cantidad_de_palabras *100 // 2 *1.3 / 100 } sengundos")

