from Funciones import *

def Intercambio(matriz, valoresOrigen, valoresDestino):
    k = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] in valoresOrigen and k < len(valoresOrigen):
                matriz[i][j] = valoresDestino[k]
                k += 1
    return matriz

A = GeneraMatriz(True)
B = GeneraMatriz(True)
print("La matriz A es: ", A)
print("La matriz B es: ", B)
minimos = Menor(A,3)
maximos = Mayor(B,3)
A = Intercambio(A, minimos, maximos)
B = Intercambio(B, maximos, minimos)
print("La matriz A tras el cambio es: ", A)
print("La matriz B tras el cambio es: ", B)