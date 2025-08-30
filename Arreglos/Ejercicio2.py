from Funciones import *

numeros = LeerNumeros(10, "numero")
promedio = Promedio([i for i in numeros if i%2==0])
print("El promedio de los numeros en las posiciones pares es:", promedio)