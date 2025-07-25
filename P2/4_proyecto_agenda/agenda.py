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
    print("\n\t\t.:: Agregar Contactos::.")
    nombre=input("Nombre del contacto: ").upper().strip()
    
    if nombre in agenda:
        print("\n\t\tEl contacto ya existe ...")
    else:
        tel=input("Telefono: ").strip()
        email=input("E-mail: ").lower().strip()
        #Agregar el atributo "nombre" al diccionario con los valores de telefono y email en una lista
        agenda[nombre]=[tel,email]
        print("\n\t\t.:: Accion realizada con exito ::.")

def mostrar_Contacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Mostrar Contacto ::.")
    print(f"{'-'*50}")
    if not agenda:
        print("\n\t\tNo existen contactos en la Agenda")
    else:
        for nombre,datos in agenda.items():
            print(f"\n\t{'Nombre: '+nombre}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail: '+datos[1]}")
            print(f"{'-'*50}")

def buscarContacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Buscar Contacto ::.")
    print(f"{'-'*50}")
    res=0
    if not agenda:
        print("\n\t\tNo existen contactos en la Agenda")
    else:
        buscar=input("\n\tIngresa el nombre del contacto a buscar: ").upper().strip()
        for i,datos in agenda.items():
            if i==buscar:
                print(f"{'-'*50}")
                print("\n\tEl contacto se ha encontrado exitosamente")
                print(f"\n\t{'Nombre: '+i}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail: '+datos[1]}\n")
                res=1
        if res==0:
            print("\n\tNo se encontro contacto con ese nombre\n")

def modificarContacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Modificar Contacto ::.")
    print(f"{'-'*50}")
    res=0
    if not agenda:
        print("\n\t\tNo existen contactos en la Agenda")
    else:
        modif=input("\n\tIngresa el nombre del contacto a modificar: ").upper().strip()
        for i,datos in agenda.items():
            if i==modif:
                print(f"{'-'*50}")
                print("\n\tEl contacto se ha encontrado exitosamente")
                print(f"\n\t{'Nombre: '+i}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail: '+datos[1]}")
                nuevo_nom=i
                op=True
                while op:
                    cambio=input(f"\t¿Deseas cambiar el nombre actual ({i})? (Si/No) ").upper().strip()
                    if cambio=="SI":
                        nuevo_nom=input("\tIngresa el nuevo valor para el nombre: ").upper().strip()
                        op=False
                    elif cambio=="NO":
                        op=False
                    else:
                        print("\tNo se ha seleccionado una opcion valida")
                nuevo_tel=datos[0]
                op=True
                while op:
                    cambio=input(f"\t¿Deseas cambiar el telefono actual ({datos[0]})? (Si/No) ").upper().strip()
                    if cambio=="SI":
                        nuevo_tel=input("\tIngresa el nuevo valor para el telefono: ").upper().strip()
                        op=False
                    elif cambio=="NO":
                        op=False
                    else:
                        print("\tNo se ha seleccionado una opcion valida")
                nuevo_mail=datos[1]
                op=True
                while op:
                    cambio=input(f"\t¿Deseas cambiar el E-mail actual ({datos[1]})? (Si/No) ").upper().strip()
                    if cambio=="SI":
                        nuevo_mail=input("\tIngresa el nuevo valor para el E-mail: ").upper().strip()
                        op=False
                    elif cambio=="NO":
                        op=False
                    else:
                        print("\tNo se ha seleccionado una opcion valida")
                res=1
                agenda[nuevo_nom]=agenda.pop(i)
                agenda[nuevo_nom]=[nuevo_tel,nuevo_mail]
                break
        if res==0:
            print("\n\tNo se encontro contacto con ese nombre\n")

def eliminarContacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Borrar Contacto ::.")
    print(f"{'-'*50}")
    if not agenda:
        print("\n\t\tNo existen contactos en la Agenda")
    else:
        elim=input("\n\tIngresa le nombre del contecto que deseas eliminar: ").upper().strip()
        for i in agenda:
            if i==elim:
                del agenda[i]
                print("Se elimino exitosamente")
                break