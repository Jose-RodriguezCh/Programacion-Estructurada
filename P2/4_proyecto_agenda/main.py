import agenda

def main():
    agenda_contactos={}
    opcion=True
    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menuPrincipal()

        if opcion=="1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="2":
            agenda.mostrar_Contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="3":
            agenda.buscarContacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="4":
            agenda.modificarContacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="5":
            agenda.eliminarContacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="6":
            print("Programa finalizado")
            opcion=False
        else:
            print("\n\t\t\u26A0 \033[31mNo se selecciono una opcion valda, vuelva a intentarlo por favor \033[0m \u26A0")
            agenda.esperarTecla()

if __name__=="__main__":
    main()