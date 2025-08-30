import random

def GeneraMatriz(aleatorio=False):
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    if aleatorio:
        matriz = [random.sample(range(101), columnas) for _ in range(filas)]
    else:
        [[input(f"Ingrese el valor de la fila {i+1} y la columna {j+1}:") for j in range(columnas)] for i in range(filas)]
    return matriz

def MayorMenor(n):
    mayor = menor = n[0]
    for i in n:
        if i > mayor:
            mayor = i
        if i < menor:
            menor = i
    return mayor, menor