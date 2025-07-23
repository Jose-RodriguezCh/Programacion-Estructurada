from paquete1 import modulos

print(modulos.saludar("Daniel C"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t.::Agenda Teledonica::.\n\tNombre: {nom}\n\tTelefono: {tel}")
modulos.esperaTecla()