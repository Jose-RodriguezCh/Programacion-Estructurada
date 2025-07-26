import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("\t\U0001F552 Oprima cualquier tecla para continuar ...\U0001F552 ")

def menu_principal():
    print("\n\t\t\t\U0001F50D...::: Sistema de calificaciones :::...\U0001F50D\n\t\t\t\t\U0001F4DD 1.- Agregar\n\t\t\t\t\U0001F4C2 2.- Mostrar\n\t\t\t\t\U0001F464 3.- Calcular promedio\n\t\t\t\t\U0001F6AA 4.- Salir")
    opcion=input("\t\t\t\t Elige una opción (1-4): ").upper()
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t\t\U0001F4DD Agregar Calificaciones \U0001F4DD\n\t\t\t")
        nombre=input("\t\U0001F464Nombre del alumno: ").upper().strip()
        lista.append(nombre)
        for i in range(1,4):
            continua=True
            while continua==True:
                try:
                    cal=float(input(f"\U0001F4DD Calificacion {i}: "))
                    if cal>=0 and cal<11:
                        lista.append(cal)
                        continua=False
                    else:
                        print("\n\t\t\t\u274C Ingresa un numero valido \u274C")
                except ValueError:
                    print("\n\t\t\t\u274C Ingresa un valor numerico \u274C")
        print("\n\t\t\t\u2705 Accion realizada con exito\u2705 ")

        try:
            cursor=conexionBD.cursor()
            sql="insert into calificaciones (nombre,calificacion_1,calificacion_2,calificacion_3) values (%s,%s,%s,%s)"
            val=(lista[0],lista[1],lista[2],lista[3])
            cursor.execute(sql,val)
            conexionBD.commit()
            print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")
            lista.clear()
        except Error as e:
            print("Error al intentar insertar un registro en la DB")
    else:
        print("No se pudo hacer conexion")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t\t\U0001F50D Mostrar calificaciones \U0001F50D\n\t\t\t")

    conexion=conectar()
    if conexion!=None:
        cursor=conexion.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t")
            print(f"{'ID':<10}{'Nombre':<15}{'Calificacion 1':<15}{'Calificacion 2':<15}{'Calificacion 3':<15}")
            print(f"-"*100)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}")
        else:
            print("No hay alumnos en el sistema")
        print(f"-"*100)

'''
def calcular_promedio(lista):
    borrarPantalla()
    acum=0
    cont=0
    print("Calcular promedio")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*40}")
        for i in lista:
            promedio=(i[1]+i[2]+i[3])/3
            print(f"{i[0]:<15}{round(promedio,2)}")
            acum+=promedio
            cont+=1
        print(f"{'-'*40}")
        print(f"El promedio de los alumnos es {(round((acum/cont),2))}")
    else:
        print("No hay calificaciones registradas en el sistema")

def calcular_promedio(lista):
    borrarPantalla()
    acum=0
    cont=0
    print("Calcular promedio")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*40}")
        promedio_grupal=0
        for i in lista:
            nombre=i[0]
            l=1
            suma=0
            while l<=3:
                suma+=i[l]
                l+=1
            promedio=suma/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio
        print(f"{'-'*40}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es: {promedio_grupal}")
    else:
        print("No hay calificaciones registradas en el sistema")
'''
def calcular_promedio(lista):
    borrarPantalla()
    print("\n\t\t\t\U0001F501 Calcular promedio \U0001F501\n\t\t\t")
    conexion=conectar()
    if conexion!=None:
        cursor=conexion.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            promedio_grupal=0
            acum=0
            print("\n\t")
            print(f"{'ID':<10}{'Nombre':<15}{'Promedio':<15}")
            print(f"-"*100)
            for i in registros:
                prom=round(((i[2]+i[3]+i[4])/3),2)
                print(f"{i[0]:<10}{i[1]:<15}{prom:<15}")
                promedio_grupal+=prom
                acum+=1
            print(f"\n\t\t\U0001F389 El promedio grupal es: {round((promedio_grupal/acum),2)} \U0001F389")
        else:
            print("No hay alumnos en el sistema")
        print(f"-"*100)

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_calificaciones"
            )
        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None
