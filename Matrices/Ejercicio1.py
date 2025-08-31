from Funciones import *

matriz = GeneraMatriz(True)
print("La matriz es:", matriz)
sumatoria = sum(map(sum,matriz))
print("La suma de los valores de la matriz es: ", sumatoria)
promedio = sumatoria/(len(matriz)*len(matriz[0]))
print("El promedio de todos los valores de la matriz es: ", promedio)
mayor = Mayor(matriz)
menor = Menor(matriz)
print("El mayor elemento de la matriz es: ", mayor, " y el menor es: ", menor)