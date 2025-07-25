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
    print("\n\t\t\t\U0001F4DD Agregar Calificaciones \U0001F4DD\n\t\t\t")
    nombre=input("\t\U0001F464Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua==True:
            try:
                cal=float(input(f"\U0001F4DD Calificacion {i}: "))
                if cal>=0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\n\t\t\t\u274C Ingresa un numero valido \u274C")
            except ValueError:
                print("\n\t\t\t\u274C Ingresa un valor numerico \u274C")
    lista.append([nombre]+calificaciones)
    print("\n\t\t\t\u2705 Accion realizada con exito\u2705 ")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t\t\U0001F50D Mostrar calificaciones \U0001F50D\n\t\t\t")
    if len(lista)>0:
        print(f"\n\t\t{'Nombre':<15}{'Calf.1':<10}{'Calf.2':<10}{'Calf.3':<10}")
        print(f"\t\t{'-'*40}")
        for i in lista:
            print(f"\t\t{i[0]:<15}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
        print(f"\t\t{'-'*40}")
        cuantos=len(lista)
        print(f"\n\t\U0001F464 Son {cuantos} alumnos")
    else:
        print("\t\t\u26A0 No hay calificaciones registradas en el sistema \u26A0")
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
    acum=0
    cont=0
    print("\n\t\t\t\U0001F501 Calcular promedio \U0001F501\n\t\t\t")
    if len(lista)>0:
        print(f"\t\t{'Alumno':<15}{'Promedio':<10}")
        print(f"\t{'-'*40}")
        promedio_grupal=0
        for i in lista:
            nombre=i[0]
            promedio=sum(i[1:])/3
            print(f"\t\t\U0001F464 {nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio
        print(f"\t{'-'*40}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"\t\t\U0001F389 El promedio grupal es: {promedio_grupal} \U0001F389")
    else:
        print("\t\t\u274C No hay calificaciones registradas en el sistema \u274C ")