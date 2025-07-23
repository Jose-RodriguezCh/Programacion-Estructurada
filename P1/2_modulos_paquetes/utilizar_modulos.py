#1er forma de utilizar los modulos
import modulos

#modulos.borrarPantalla
print(modulos.saludar("Elchavo"))

#2da forma de utilizar moulos
from modulos import * #Para todas las funciones
from modulos import saludar,borrarPantalla #Para funciones especificas

#borrarPantalla()
print(saludar("Elchavodel8"))



nombre=input("Ingresa el nombre del contacto ")
telefono=input("Ingresa su numero de telefono con clave lada ")
nom,tel=modulos.solicitarDatos4(nombre,telefono)
print(f"\tNombre Completo: {nom} \nTelefono: {tel}")

