from Funciones import *

R = GeneraMatriz(True)
S = GeneraMatriz(True)
elementosComunes = [i for fila in R for i in fila if i in [j for fila2 in S for j in fila2]]
if len(elementosComunes) == 1:
    elementosComunes = elementosComunes[0]
print("Los elementos comunes entre las dos matrices son: ", elementosComunes)