'''
Un módulo es simplemente un archivo con extension .py que contiene codigo de Python (funciones, clases, variables, etc.).
Un paquete es una carpeta que contiene varios modulos (archivos .py) y un archivo especial llamado: __init__.py
que le indicaa python que esa carpeta debe de tratarse como un paquete
'''

import os

def solicitarDatos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"Soy funcion 1- El nombre es: {nombre} y su telefono es: {telefono}")

def solicitarDatos3(nombre,tel):
    nom=nombre
    telefono=tel
    print(f"Soy funcion 3- El nombre es: {nom} y su telefono es: {telefono}")

'''nombre=input("Nombre: ")
telefono=input("Telefono: ")'''

def solicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    '''resp=f"El nombre es: {nombre} y su telefono es: {telefono}"
    return resp'''
    '''return nombre,telefono'''
    return f"El nombre es: {nombre} y su telefono es: {telefono}"

def solicitarDatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom,tel

def borrarPantalla():
    os.system("cls")

def esperaTecla():
    input("...Oprima una tecla para continuar...")

def saludar(nombre):
    nom=nombre
    return f"Hola, bienvenido: {nom}"