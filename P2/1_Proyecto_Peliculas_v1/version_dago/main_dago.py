import os
import peliculas_dago

opcion=True
while opcion:
    peliculas_dago.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_dago.agregarPeliculas()
            peliculas_dago.esperarTecla()
        case "2":
            peliculas_dago.eliminarPeliculas()
            peliculas_dago.esperarTecla()
        case "3":
            peliculas_dago.modificarPeliculas()
            peliculas_dago.esperarTecla()
        case "4":
            peliculas_dago.consultarPeliculas()
            peliculas_dago.esperarTecla()
        case "5": 
            peliculas_dago.buscarPeliculas()
            peliculas_dago.esperarTecla()
        case "6":
            peliculas_dago.vaciarPeliculas()
            peliculas_dago.esperarTecla
        case "7":
            opcion=False
            peliculas_dago.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")