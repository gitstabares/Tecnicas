import random

def GeneraMatriz(aleatorio=False):
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    if aleatorio:
        matriz = [random.sample(range(101), columnas) for _ in range(filas)]
    else:
        [[input(f"Ingrese el valor de la fila {i+1} y la columna {j+1}:") for j in range(columnas)] for i in range(filas)]
    return matriz

def GeneraVector(aleatorio=False):
    longitud = int(input("Ingrese la longitud del vector: "))
    if aleatorio:
        vector = random.sample(range(101), longitud)
    else:
        vector = [input(f"Ingrese el valor {i+1} del vector:") for i in range(longitud)]
    return vector

def Mayor(matriz,cantidad=1):
    elementos = [elemento for fila in matriz for elemento in fila]
    elementos.sort()
    mayor = elementos[-cantidad:]
    if len(mayor) == 1:
        return mayor[0]
    return mayor

def Menor(matriz,cantidad=1):
    elementos = [elemento for fila in matriz for elemento in fila]
    elementos.sort()
    menor = elementos[:cantidad]
    if len(menor) == 1:
        return menor[0]
    return menor