'''
Proyecto 1
Crear un proyecto que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar  consultar peliculas.

Notas
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar dict para almacenar los siguientes atributos: (nombre,categoria,clasificacion,genero,idioma) de las peliculas
3.- Utilizar e implementar una BD para festionar las peliculas
'''

import os
import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear \U0001F4DD \n\t\t 2.- Borrar \U0001F4DB\n\t\t 3.- Mostrar \U0001F4C2\n\t\t 4.- Modificar \U0001F501\n\t\t 5.- Buscar \n\t\t 6.- SALIR\U0001F6AA")
    opcion=input("\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion=False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")