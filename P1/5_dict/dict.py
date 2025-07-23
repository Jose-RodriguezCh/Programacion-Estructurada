'''
dict.-
Es un tipo de datos que se utiliza para almacenar datos de
diferente tipo de datos pero en lugar de tener como las 
listas indices numericos tiene alfanumericos. Es decir, es
algo parecido como los objetos.

Tambien se conoce como un arreglo asociativo u objeto JSON

El diccionario es una colección ordenada** y modificable. No
hay miembros duplicados.

'''
import os
os.system("cls")

#Lista
#paises=["Mexico","Brazil","Canada","España"]

#Dict. o Objeto
pais_mexico={"nombre":"Mexico",
        "Capital":"CDMEX",
        "poblacion":"12000000",
        "idioma":"español",
        "status":True}

pais_brasil={"nombre":"Brazil",
        "Capital":"Brazilia",
        "poblacion":"0",
        "idioma":"Portugues",
        "status":True}

pais_canada={"nombre":"Canada",
        "Capital":"Ottawa",
        "poblacion":"900000"
        ,"idioma":["Ingles","frances"],
        "status":False}

alumno1={
    "nombre":"Daniel",
    "apellido_paterno":"Hernandez",
    "apellido_materno":"Gonzalez",
    "carrera":"TI",
    "area":"Software Multiplataforma",
    "modalidad":"Bilingue",
    "matricula":"123456",
    "semestre":"2"
}

#Mostrar el contenido del dict
print(alumno1)

for i in alumno1:
    print(f"{i}={alumno1[i]}")

#Agregar un campo o atributo
alumno1["telefono"]="6181234567"
for i in alumno1:
    print(f"{i}={alumno1[i]}")