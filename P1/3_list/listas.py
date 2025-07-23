import os
#Ejemplo 1. Crear una lista de numeros e imprimir el contenido

numeros=[23,45,56,78]

print(numeros)
for i in numeros:
    print(i)
for i in range(0,len(numeros)):
    print(numeros[i])

#Ejemplo 2. Crear una lista de palabras y posteriormente buscar la coincidencia de una palabre
os.system("cls")
palabras=["Mercurio","Venus","Tierra","Marte"]

#1er Forma
print(palabras)
pal=input("¿Que palabra deseas buscar? ")
if pal in palabras:
    print(f"La palabra {pal} Si se encontro en la lista")
else:
    print(f"La palabra {pal} no se encontro en la lista")

#2da Forma
encontro=False
for i in palabras:
    if i==pal:
        encontro=True
if encontro:
    veces=palabras.count(pal)
    print(f"La palabra {pal} Si se encontro {veces} veces en la lista")
else:
    print(f"La palabra {pal} no se encontro en la lista")

#3er Froma
encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==pal:
        encontro=True
if encontro:
    print(f"La palabra {pal} Si se encontro en la lista")
else:
    print(f"La palabra {pal} no se encontro en la lista")

input("Oprima una tecla")

#Ejemplo 3. Añadir elementos a una lista
os.system("cls")

numeros=[]
print(numeros)
opc=True
while opc==True:
    numero=float(input("Dame un numero entero o decimal: "))
    numeros.append(numero)
    resp=input("¿Deseas agragar otro numero? ").lower()
    if resp=="si":
        opc=True
    else:
        opc=False

print(numeros)
input("Oprima una tecla")

#Ejemplo 4. Crear una lista multidimensional que sea una agenda
agenda=[
    ["Carlos","6181234567"],
    ["Alberto","6671234567"],
    ["Martin","6785678923"]
    ]

print(agenda)
for i in agenda:
    print(i)

res=""
for r in range(0,3):
    res=""
    for c in range(0,2):
        res+=(f"{agenda[r][c]}\t")
    print(res)
