import mysql.connector
from mysql.connector import Error
def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("\t\U0001F552 Oprima cualquier tecla para continuar ...\U0001F552 ")

def menuPrincipal():
    print("\n\t\t\U0001F464 ..::: Sistema de Gestion de Agenda de Contactos :::.. \U0001F464\n")
    print("\t\t\t1 Agregar contacto " \
        "\n\t\t\t2 Mostrar todos los contactos " \
        "\n\t\t\t3 Buscar contacto por nombre " \
        "\n\t\t\t4 Modificar contacto" \
        "\n\t\t\t5 Eliminar contacto" \
        "\n\t\t\t6 SALIR")
    op=input("\n\t\t\t Elige una opcion (1-6): ")
    return op

def agregar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t.:: Agregar Contactos::.")
        print(f"{'-'*50}")
        nombre=input("Nombre del contacto: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="SELECT * FROM contactos WHERE nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        
        contacto=cursor.fetchall()
        if len(contacto)>0:
            print("\n\t\tEl contacto ya existe ...")
        else:
            continua=True
            while continua:
                try:
                    tel=int(input("Telefono: ").strip())
                    if len(str(abs(tel)))>0 and len(str(abs(tel)))<11:
                        continua=False
                    else:
                        print("\t\t\t\u274C Ingresa un numero de 10 digitos \u274C")
                except ValueError:
                    print("\t\t\t\u274C Ingresa un valor numerico entero\u274C")
            email=input("E-mail: ").lower().strip()
            #Agregar el atributo "nombre" al diccionario con los valores de telefono y email en una lista
            agenda[nombre]=[tel,email]
            try:
                sql="insert into contactos (nombre,telefono,email) values (%s,%s,%s)"
                val=(nombre,tel,email)
                cursor.execute(sql,val)
                conexionBD.commit()
                print("\n\t\t.::\u2705 LA OPERACION SE REALIZO CON EXITO \u2705::.")
            except Error as e:
                print("Error al intentar insertar un registro en la DB")
    else:
        print("No se pudo hacer conexion")

def mostrar_Contacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Mostrar Contacto ::.")
    print(f"{'-'*50}")
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        sql="SELECT * FROM contactos"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*100)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}")
            print(f"-"*100)
        else:
            print("\n\t\tNo existen contactos en la Agenda")
    else:
        print("No se pudo hacer conexion")
        print(f"-"*100)

    

def buscarContacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Buscar Contacto ::.")
    print(f"{'-'*50}")

    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        sql="SELECT * FROM contactos"
        cursor.execute(sql)
        registros=cursor.fetchall()
        res=0
        if registros:
            buscar=input("\n\tIngresa el nombre del contacto a buscar: ").upper().strip()
            print
            for i in registros:
                if i[1]==buscar:
                    print("\n\tEl contacto se ha encontrado exitosamente")
                    print(f"{'-'*50}")
                    print(f"\n\tNombre: {i[1]}\n\tTelefono: {i[2]}\n\tE-mail: {i[3]}\n")
                    res=1
                    print(f"{'-'*50}")
            if res==0:
                print("\n\tNo se encontro contacto con ese nombre\n")
        else:
            print("\n\t\tNo existen contactos en la Agenda")
    else:
        print("No se pudo hacer conexion")
        print(f"-"*100)
    
    
        

def modificarContacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    print("\n\t\t.:: Modificar Contacto ::.")
    print(f"{'-'*50}")
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        sql="SELECT * FROM contactos"
        cursor.execute(sql)
        registros=cursor.fetchall()
        res=0
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*100)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}")
            print(f"-"*100)
            op=True
            while op:
                opcion=input("\t¿Deseas modificar algun contacto? (Si/No)").upper().strip()
                if opcion=="SI":
                    buscar=input("\tIngresa el nombre del contacto a modificar: ").upper().strip()
                    for i in registros:
                        if i[1]==buscar:
                            nuevo_nom=i[1]
                            op=True
                            while op:
                                cambio=input(f"\t¿Deseas cambiar el nombre actual ({i[1]})? (Si/No) ").upper().strip()
                                if cambio=="SI":
                                    nuevo_nom=input("\tIngresa el nuevo valor para el nombre: ").upper().strip()
                                    op=False
                                elif cambio=="NO":
                                    op=False
                                else:
                                    print("\tNo se ha seleccionado una opcion valida")
                            nuevo_tel=i[2]
                            op=True
                            while op:
                                cambio=input(f"\t¿Deseas cambiar el telefono actual ({i[2]})? (Si/No) ").upper().strip()
                                if cambio=="SI":
                                    continua=True
                                    while continua:
                                        try:
                                            nuevo_tel=int(input("\tIngresa el nuevo valor para el telefono: ").strip())
                                            if len(str(abs(nuevo_tel)))>0 and len(str(abs(nuevo_tel)))<11:
                                                continua=False
                                            else:
                                                print("\t\t\t\u274C Ingresa un numero de 10 digitos \u274C")
                                        except ValueError:
                                            print("\t\t\t\u274C Ingresa un valor numerico entero\u274C")
                                    op=False
                                elif cambio=="NO":
                                    op=False
                                else:
                                    print("\tNo se ha seleccionado una opcion valida")
                            nuevo_mail=i[3]
                            op=True
                            while op:
                                cambio=input(f"\t¿Deseas cambiar el E-mail actual ({i[3]})? (Si/No) ").upper().strip()
                                if cambio=="SI":
                                    nuevo_mail=input("\tIngresa el nuevo valor para el E-mail: ").upper().strip()
                                    op=False
                                elif cambio=="NO":
                                    op=False
                                else:
                                    print("\tNo se ha seleccionado una opcion valida")
                            res=1
                            sql="UPDATE contactos SET nombre=%s,telefono=%s,email=%s WHERE id=%s"
                            val=(nuevo_nom,nuevo_tel,nuevo_mail,i[0])
                            cursor.execute(sql,val)
                            conexionBD.commit()
                            print("\n\t\tLa modificacion fue exitosa")
                    if res==0:
                        print("\tNo se encontro el contacto con ese nombre\n")
                        op=False
                elif opcion=="NO":
                    print("\n\tLa operacion se cancelo\n")
                    op=False
                else:
                    print("\tNo se selecciono una opcion valida\n")
        else:
            print("\n\t\tNo existen contactos en la Agenda")
    else:
        print("No se pudo hacer conexion")
        print(f"-"*100)



                
    

def eliminarContacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Borrar Contacto ::.")
    print(f"{'-'*50}")
    conexion=conectar()
    if conexion!=None:
        cursor=conexion.cursor()
        sql="SELECT * FROM contactos"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t")
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<15}")
            print(f"-"*100)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}")
            print(f"-"*100)
            op=True
            while op:
                opcion=input("¿Deseas eliminar un contacto? (Si/No)").upper().strip()
                if opcion=="SI":
                    elim=input("\n\tIngresa le nombre del contecto que deseas eliminar: ").upper().strip()
                    for i in registros:
                        if i[1]==elim:
                            sql="DELETE FROM contactos WHERE nombre=%s"
                            val=(elim,)
                            cursor.execute(sql,val)
                            conexion.commit()
                            print("\tSe elimino exitosamente")
                            break
                        else:
                            print("\n\tNo se selecciono una opcion valida")
                    op=False
                elif opcion=="NO":
                    print("\tSe ha cancelado la operacion\n")
                    op=False
                else:
                    print("No se ha seleccionado una opcion valida")
        else:
            print("No hay contactos en la agenda")

        

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_agenda"
            )
        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None
