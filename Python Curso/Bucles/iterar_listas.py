animales = ["Pez","Perro","Gato","Cocodrilo"]
numeros = [10,25,47,54]

#recorriendo la lista de animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

#recorriendo la lista numeros y multtiplicando cada valor * 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")