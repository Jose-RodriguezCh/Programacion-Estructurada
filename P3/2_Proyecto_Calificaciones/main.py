'''
Proyecto 3
Crear un proyecto que permita Gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estidiante.

Notas
1.- Utilizar funciones y mandar llamar desde otro archivo (modulos)
2.- Utilizar list (bidimensional) para almacenar el nombre del alumno, así como sus 3 calificaciones.
'''

import calificaciones

def main():
    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedio(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion=False
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                input("\n\t\u26A0 \033[31m Opción invalida vuelva a intentarlo ... por favor \033[0m\u26A0 ")

if __name__=="__main__":
    main()