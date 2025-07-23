'''
List (Array)
Son colecciones o conjunto de datos/valores bajo
un mismo nombre, pero acceder a los valores se 
hace con un indice numerico.

Notar: Sus valores si son modificanles.

La lista en una coleccion ordenada y modificable. Permite miembros duplicados.

'''
import os
os.system("cls")

#Funciones mas comunes en las listas
paises=["México","Brasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#Añadir o ingresar o insertar elementos a una lista
#1er. Forma
paises.append("Honduras")
#2da. Forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o borrar o quitar elementos de una lista
#1er Forma con el indice
paises.pop(1)
print(paises)
#2da Forma con el valor
paises.remove("Honduras")
print(paises)

#Buscar elemento dentro de una lista
#1er Forma
resp="Brasil" in paises
if resp:
    print("Si encontre el pais")
else:
    print("No encontre el pais")

paises=["México","Brasil","España","Canada"]

#2ds Forma
for i in range(0,len(paises)):
    if paises[i]=="Brasil":
        print("Si encontro el pais")
    else:
        print("No se encotro el pais")

#Cuantas veces aparece un elemento dentro de una lista

#numeros=[23,12,100,34]

print(f"Este numero 12 aparece: {numeros.count(12)} veces")
numeros.append(12)
print(f"Este numero 12 aparece: {numeros.count(12)} veces")

#Identificar o conocer el indice de un valor

#paises=["México","Brasil","España","Canada"]
indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de una lista
#1er Forma con los valores
for i in paises:
    print(i)

#2ds Forma con los indices
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")

#Unir contenido de listas
#paises=["México","Brasil","España","Canada"]
#numeros=[23,12,100,34,12]
print(paises)
print(numeros)

paises.extend(numeros)