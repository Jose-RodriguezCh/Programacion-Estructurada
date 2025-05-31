'''Una funcion es un conjunto de instrucciones agrupados bajo un nombre en
particular como un programa mas pequeño que cumple una funcion especifica. La
funcion de puede reutilizar con el simple hecho de invocarla, es decir 
mandarla a llamar.

Sintaxis

def nombredeMifuncion(parametros):
    bloque o conjunto de instrucciones

nombredeMifuncion(parametros)

Las funciones pueden ser de 4 tipo

Funciones de tipo "procedimiento":
1.- Funcion que no recibe parametros y no regresa valor
3.- Funcion que recibe parametros y no regresa valor 

Funciones de tipo "funcion":
2.- Funcion que no recibe parametros y regresa valor
4.- Funcion que recibe parametros y regresa valor
'''

#1.- Funcion que no recibe parametros y no regresa valor
def solicitarDatos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"Soy funcion 1- El nombre es: {nombre} y su telefono es: {telefono}")

#3.- Funcion que recibe parametros y no regresa valor
def solicitarDatos3(nombre,tel):
    nom=nombre
    telefono=tel
    print(f"Soy funcion 3- El nombre es: {nom} y su telefono es: {telefono}")

'''nombre=input("Nombre: ")
telefono=input("Telefono: ")'''

#2.- Funcion que no recibe parametros y regresa valor
def solicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    '''resp=f"El nombre es: {nombre} y su telefono es: {telefono}"
    return resp'''
    '''return nombre,telefono'''
    return f"El nombre es: {nombre} y su telefono es: {telefono}"

#4.- Funcion que recibe parametros y regresa valor
def solicitarDatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom,tel

#Llamar mis funciones
print("Funcion 1")
solicitarDatos1()

print("\nFuncion 3")
nom3=input("Nombre: ")
tel3=input("Telefono: ")
solicitarDatos3(nom3,tel3)

print("\nFuncion 2")
nom2,tel2=solicitarDatos2()
print(f"Nombre: {nom2}\n Telefono: {tel2}")

print("\nFuncion 4")
nom4=input("Nombre: ")
tel4=input("Telefono: ")
nombre4,telefono4=solicitarDatos4(nom4,tel4)
print(f"Nombre: {nombre4}\n Telefono: {telefono4}")