from Funciones import *

A = GeneraMatriz()
V = GeneraVector()

for j in range(len(A[0])):
    columna = [A[i][j] for i in range(len(A))]
    if columna == V:
        print(f"La columna {j} de la matriz A es igual al vector V.")
        break
else:
    print("Ninguna columna de la matriz A es igual al vector V.")