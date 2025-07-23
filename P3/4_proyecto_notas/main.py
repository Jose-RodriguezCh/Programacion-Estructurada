import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\t{nombre} {apellidos}, se registro correctamente, con el email {email}")
            else:
              print(f"\n\t...Por favor intentelo denuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            registro=usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\tE-mail y/o contraseña incorrectas, vuelva a intentarlo...")
            funciones.esperarTecla()
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"\n\tSe creo la nota {titulo} exitosamente")
            else:
                print(f"\n\tNo fue posible crear la nota en este momento, vuelva a intentar ...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print("\n\tMostrar las notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*50)
                for i in lista_notas:
                    print(f"{i[0]:<10}{i[2]:<15}{i[3]:<15}{i[4]}")  
                print(f"-"*50)
            else:
                print("\n\tNo existen notas de acuerdo a ese usuario")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print("\n\tMostrar las notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*50)
                for i in lista_notas:
                    print(f"{i[0]:<10}{i[2]:<15}{i[3]:<15}{i[4]}")  
                print(f"-"*50)
                op=True
                while op:
                    cambio=input("¿Deseas cambiar alguna lista? (Si/No): ").upper().strip()
                    if cambio=="SI":
                        id = input("\t \t ID de la nota a actualizar: ")
                        res=False
                        for i in lista_notas:
                            if str(i[0])==id:
                                res=True
                        if res:
                            titulo = input("\t Nuevo título: ")
                            descripcion = input("\t Nueva descripción: ")
                            #Agregar codigo
                            respuesta=nota.cambiar(id,titulo,descripcion)
                            if respuesta:
                                print(f"\n\tSe actualizo la nota {titulo} exitosamente")
                            else:
                                print(f"\n\tNo fue posible actualizar la nota en este momento, vuelva a intentar ...")  
                        else:
                            print(f"\n\tNo hay notas con el id {id} en el sistema, vuelva a intentarlo...")
                        op=False
                    elif cambio=="NO":
                        op=False
                    else:
                        print("No se selecciono una opcion valida, volver a intentarlo")
            else:
                print("\n\tNo existen notas de acuerdo a ese usuario")
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print("\n\tMostrar las notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*50)
                for i in lista_notas:
                    print(f"{i[0]:<10}{i[2]:<15}{i[3]:<15}{i[4]}")  
                print(f"-"*50)
                print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                op=True
                while op:
                    res=input("¿Deseas borrar alguna nota? (Si/No)").upper().strip()
                    if res=="SI":
                        id = input("\t \t ID de la nota a eliminar: ")
                        #Agregar codigo
                        respuesta=nota.borrar(id)
                        if respuesta:
                            print(f"Se borro la nota {id} exitosamente")
                        elif respuesta==False:
                            print(f"No fue posible borrar la nota en este momento, vuelva a intentar ...")
                        op=False
                    elif res=="NO":
                        op=False
                    else:
                        print("No se selecciono una opcion valida")
            else:
                print("\n\tNo existen notas de acuerdo a ese usuario")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


