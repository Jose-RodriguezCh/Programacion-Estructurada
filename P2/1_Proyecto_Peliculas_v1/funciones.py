import os
def limpiar_pantalla():
    os.system("cls")

def consultar(peliculas):
    for i in range(0,len(peliculas)):
        print(f"\t{i+1} : {peliculas[i]}")
    busc=input("Teclea la pelicula a buscar: ")
    n=False
    for i in peliculas:
        if busc.upper()==i.upper():
            n=True
    if n==True:
        print("Se encontro la pelicula")
    else:
        print("No se encontro la pelicula")

def agregar_pelicula(peliculas):
    nueva_pelicula=input("Teclea el nombre de la pelicula ")
    print(f"La pelicula {nueva_pelicula} a sido agregada exitosamente")
    return nueva_pelicula

def eliminar_pelicula(peliculas):
    eliminar_pelicula=(int(input("Teclea el numero de la pelicula que deseas eliminar: "))-1)
    print(f"La pelicula {peliculas[eliminar_pelicula]} se a eliminado exitosamente")
    return eliminar_pelicula

def modificar_peliculas(peliculas):
    modificar_pelicula=(int(input("Teclea el numero de la pelicula que deseas modificar: "))-1)
    pelicula_modificada=input("Ingresa el nuevo nombre de la pelicula: ")
    print(f"La pelicula {peliculas[modificar_pelicula]} se a cambiado a {pelicula_modificada} exitosamente")
    return modificar_pelicula,pelicula_modificada