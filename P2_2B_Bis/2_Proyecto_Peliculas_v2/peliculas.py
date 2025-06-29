peliculas=[]

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
'''pelicula={
    "nombre":"",
    "categoria":"",
    "clasificacion":"",
    "genero":"",
    "idioma":""
}
'''
pelicula={}

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar ...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Peliculas ::. \n")
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la Pelicula ::. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t {i} : {pelicula[i]}")
    else:
        print("No hay peliculas en el sistema")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar TODAS las Peliculas ::. \n")
    resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (Si/No)").upper().strip()
    if resp=="si":
        pelicula.clear()
        print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Caracteristica a Peliculas ::. \n")
    atributo=input("Ingresa la nueva caracteristica de la pelicula: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    #pelicula.update({atributo:valor})
    pelicula[atributo]=valor
    print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Caracteristica a Peliculas ::. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t {i} : {pelicula[i]}")
            resp=input(f"\t ¿Deseas cambiar el valor de {i}? (si/no)").upper().strip()
            if resp=="SI":
                atributo=input(f"Ingresa el nuevo valor de la caracteristica '{i}' de la pelicula: ").upper().strip()
                pelicula.update({{f"{i}"}:f"{atributo}"})
        print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")
    else:
        print("No hay peliculas en el sistema")
    
def vaciarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar caracteristica de Peliculas ::. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t {i} : {pelicula[i]}")
        opc=True
        while opc:
            valor=input("¿Deseas borrar una caracteristica? (Si/No)").lower().strip()
            if valor=="si":
                atributo=input("\U0001F50D Ingresa la caracteristica a borrar de la pelicula: ").lower().strip()
                for i in pelicula:
                    if i==atributo:
                        pelicula.pop(i)
                        i=i-1
            else:
                print("Se ha cancelado la operacion")
    else:
        print("No hay peliculas en el sistema")
#def consultarPeliculas():
    borrarPantalla()
    print(".:: Consultar Peliculas ::.")
    if len(peliculas)>0:
        for i in range(0,len(peliculas)):
            print(f"{i+1}: {peliculas[i]}")
    else:
        print("\t ..:: No hay peliculas en el sistema ::..")

#def vaciarPeliculas():
    borrarPantalla()
    print("\n\t .:: Borrar o quitar todas las peliculas ::.")
    resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (SI/NO)").lower()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t.:: LA OPERACION SE REALIZO CON EXITO::.")

#def buscarPeliculas():
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

#def eliminarPeliculas():
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