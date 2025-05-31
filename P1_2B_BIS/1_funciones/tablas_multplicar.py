'''
Crear un programa que calcule e imprima cualquier tabla de multiplicar
Requisitos:
1.- Sin estructuras de control
2.- Sin funciones
'''
'''
dato=int(input("Teclea el numero de la tabla de multiplicar a calcular"))
print(f"\nTabla de multiplicar del {dato}\n")
num=dato*1
print(f"{dato} X 1 = {num}")
num=dato*2
print(f"{dato} X 2 = {num}")
num=dato*3
print(f"{dato} X 3 = {num}")
num=dato*4
print(f"{dato} X 4 = {num}")
num=dato*5
print(f"{dato} X 5 = {num}")
num=dato*6
print(f"{dato} X 6 = {num}")
num=dato*7
print(f"{dato} X 7 = {num}")
num=dato*8
print(f"{dato} X 8 = {num}")
num=dato*9
print(f"{dato} X 9 = {num}")
num=dato*10
print(f"{dato} X 10 = {num}")
'''
'''
#Version 3
dato=int(input("Teclea el numero de la tabla de multiplicar a calcular "))
print(f"\nTabla de multiplicar del {dato}\n")
for i in range(1,11):
    multi=dato*i
    print(f"{dato} X {i} = {multi}")

dato=int(input("Teclea el numero de la tabla de multiplicar a calcular "))
print(f"\nTabla de multiplicar del {dato}\n")
i=1
while i<=10:
    multi=dato*i
    print(f"{dato} X {i} = {multi}")
    i+=1
'''
#Varsion 4
#Con funciones que regresa valor y utilice parametros
def op1(dato):
    resultado=""
    for i in range(1,11):
        multi=dato*i
        resultado+=f"{dato} X {i} = {multi}\n"
    return resultado

dato=int(input("Teclea el numero de la tabla de multiplicar a calcular "))
print(f"\nTabla de multiplicar del {dato}\n")
resultado=op1(dato)
print(resultado)

print("\n----------------------------------------------------------------------\n")

def op2(dato):
    i=1
    while i<=10:
        multi=dato*i
        print(f"{dato} X {i} = {multi}")
        i+=1

dato=int(input("Teclea el numero de la tabla de multiplicar a calcular "))
print(f"\nTabla de multiplicar del {dato}\n")
op2(dato)