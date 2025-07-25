'''
Crear un proyecto que permita gestionar (Administrar) peliculas, colocar un numero de opciones para 
agregar, eliminar, modificar y consultar peliculas.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo.
2.- Utilizar listas para almacenar los nombres de las peliculas.
3.- 
'''

import os
import funciones
funciones.limpiar_pantalla()

peliculas=[]
n=True
while n==True:
    funciones.limpiar_pantalla()
    opcion=input("\t1.- Agregar pelicula\n\t2.-Eliminar pelicula\n\t3.-Modificar pelicula\n\t4.-Consultar pelicula\n\t5.-Salir\n\nTeclea la opcion deseada\n")
    match opcion:
        case "1":
            funciones.limpiar_pantalla()
            peliculas.append(funciones.agregar_pelicula(peliculas))
            input("Presiona cualquier tecla para continuar")
        case "2":
            funciones.limpiar_pantalla()
            funciones.consultar(peliculas)
            peliculas.pop(funciones.eliminar_pelicula(peliculas))
            input("Presiona cualquier tecla para continuar")
        case "3":
            funciones.limpiar_pantalla()
            funciones.consultar(peliculas)
            mod_peli,peli_mod=funciones.modificar_peliculas(peliculas)
            peliculas.pop(mod_peli)
            peliculas.insert(mod_peli,peli_mod)
            input("Presiona cualquier tecla para continuar")
        case "4":
            print("Peliculas disponibles")
            funciones.limpiar_pantalla()
            funciones.consultar(peliculas)
            input("Presiona cualquier tecla para continuar")
        case "5":
            n=False
        case _:
            input("No se ha tecleado una opcion valida\nPresiona cualquier tecla para volver a intentar")
print("Se ha terminado la ejecucion")
