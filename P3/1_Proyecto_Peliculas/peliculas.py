import mysql.connector
from mysql.connector import Error
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
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.:: Alta de Peliculas ::. \n")
        pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
        pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
        pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
        pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
        pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})

        ######## Agregar Registros a la DB
        try:
            cursor=conexionBD.cursor()
            sql="insert into peliculas (id,nombre,categoria,clasificacion,genero,idioma) values (null,%s,%s,%s,%s,%s)"
            val=(pelicula['nombre'],pelicula['categoria'],pelicula['clasificacion'],pelicula['genero'],pelicula['idioma'])
            cursor.execute(sql,val)
            conexionBD.commit()
            print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")
        except Error as e:
            print("Error al intentar insertar un registro en la DB")
    else:
        print("No se pudo hacer conexion")

def modificarPeliculas():
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: Modificar una Pelicula ::. \n")
        cursor=conexion.cursor()
        sql="select * from peliculas where nombre=%s"
        nombre=input("Dame el nombre de la pelicula a modificar: ").upper().strip()
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        #registros=cursor.fetchone() //Cuando hay un solo registro con ese id o nombre
        if registros:
            print("\n\tMostrar las peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*50)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
            print(f"-"*50)
            resp=input("¿Deseas modiificar la pelicula? (So/No)").lower().strip()
            if resp=="si":
                pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
                pelicula["categoria"]=input("Ingresa la categoria: ").upper().strip()
                pelicula["clasificacion"]=input("Ingresa la clasificacion: ").upper().strip()
                pelicula["genero"]=input("Ingresa el genero: ").upper().strip()
                pelicula["idioma"]=input("Ingresa el idioma: ").upper().strip()
                sql="UPDATE peliculas SET nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s WHERE nombre=%s"
                val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"],nombre)
                cursor.execute(sql,val)
                conexion.commit()
        else:
            print("\n\t\tLa pelicula a modificar no se encuentra en el sistema")

def mostrarPeliculas():
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: Consultar o Mostrar la Pelicula ::. \n")
        cursor=conexion.cursor()
        sql="select * from peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\tMostrar las peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*50)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
        else:
            print("No hay peliculas en el sistema")
        print(f"-"*50)
        '''if len(pelicula)>0:
            for i in pelicula:
                print(f"\t {i} : {pelicula[i]}")
        else:
            print("No hay peliculas en el sistema")'''

def borrarPeliculas():
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: Borrar una Pelicula ::. \n")
        cursor=conexion.cursor()
        nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\tMostrar las peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*50)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
            print(f"-"*50)
            resp=input(f"¿Deseas borrar la pelicula de {nombre}? (Si/No): ").lower().strip()
            if resp=="si":
                sql="DELETE FROM peliculas where nombre=%s"
                val=(nombre,)
                cursor.execute(sql,val)
                conexion.commit()
                print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")
        else:
            print("\n\t\tLa pelicula a borrar no se encuentra en el sistema")

def buscarPeliculas():
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: Buscar una Pelicula ::. \n")
        cursor=conexion.cursor()
        sql="select * from peliculas where nombre=%s"
        nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        #registros=cursor.fetchone() //Cuando hay un solo registro con ese id o nombre
        if registros:
            print("\n\tMostrar las peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*50)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
            print(f"-"*50)
        else:
            print("\n\t\tLa pelicula a buscar no se encuentra")
        


def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_peliculas"
            )
        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None
