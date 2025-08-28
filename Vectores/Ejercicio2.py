from Funciones import Leer, Promedio

numeros = Leer(10, "numero")
promedio = Promedio([i for i in numeros if i%2==0])
print(promedio)