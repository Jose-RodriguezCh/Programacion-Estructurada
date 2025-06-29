peliculas=[]

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    print("Oprima cualquier tecla para continuar ...")
    input()  

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Peliculas ::. ")
    peliculas.append(input("Ingresa el nombre: ").upper().strip())
    print("\n\t\t.:: LA OPERACION SE REALIZO CON EXITO::.")

def consultarPeliculas():
    borrarPantalla()
    print(".:: Consultar Peliculas ::.")
    if len(peliculas)>0:
        for i in range(0,len(peliculas)):
            print(f"{i+1}: {peliculas[i]}")
    else:
        print("\t ..:: No hay peliculas en el sistema ::..")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t .:: Borrar o quitar todas las peliculas ::.")
    resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (SI/NO)").lower()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t.:: LA OPERACION SE REALIZO CON EXITO::.")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t .:: Buscar Peliculas ::.")
    pelicula_buscar=input("Ingresa el nombre de la pelicula a buscar").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t\t ¡No se encuentra la pelicula a buscar!")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
                encontro+=1
        print(f"Tenemos {encontro} peliculas con este titulo")
        print("\n\t\t.:: LA OPERACION SE REALIZO CON EXITO::.")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t .:: Eliminar Pelicula ::.")
    pelicula_eliminar=input("Ingresa el nombre de la pelicula que deseas eliminar").upper().strip()
    encontro=0
    if not(pelicula_eliminar in peliculas):
        print("\n\t\t ¡No se encuentra la pelicula a eliminar!")
    else:
        for i in range(0,len(peliculas)):
            i=i-encontro
            if pelicula_eliminar==peliculas[i]:
                resp=input("¿Deseas quitar o borrar la pelicula del sistema? (SI/NO)").lower()
                if resp=="si":
                    print(f"La pelicula que se borro es: {pelicula_eliminar} y estaba en la casilla {i+1} ")
                    peliculas.pop(i)
                    print("\n\t\t.:: LA OPERACION SE REALIZO CON EXITO::.")
                    encontro+=1
                else:
                    print("No se elimino la pelicula")
        print(f"Se borro {encontro} pelicula(s) con este titulo")