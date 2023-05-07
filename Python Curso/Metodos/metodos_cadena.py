cadena1 = "hola,Mundo,como,amanecemos"
cadena2 = "WELCOME CRACK"

#Convierte todo el texto en Mayusculas
resultado = cadena1.upper()
print(resultado)

#Convierte a Minusculas
resultado2 = cadena2.lower()
print(resultado2)

#Primer letra en Mayuscula y deja las demas en minuscula
primer_letra_mayus = cadena1.capitalize()
print(primer_letra_mayus)

#Buscamos una cadena en otra cadena (-1 = No existe)
busqueda_find = cadena1.find("a")
print(busqueda_find)

#Buscamos una cadena en otra cadena (Nos lanza una excepcion)
busqueda_index = cadena1.index("a")
print(busqueda_index)

#si es nuerico devuelve true, si no false.
es_numerico = cadena1.isnumeric()
print(es_numerico)

#si es alfa numerico devuelve true, si no es false (A-Z)
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)

#contamos cuantos caracteres tiene una cadena 
contar_caracteres = len (cadena1)
print(contar_caracteres)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
emmpieza_con = cadena1.startswith("h")
print(emmpieza_con)

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("o")
print(termina_con)

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("hola Mundo","holu Mundito") 
print(cadena_nueva)

#Separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(",")
print(cadena_separada[1])