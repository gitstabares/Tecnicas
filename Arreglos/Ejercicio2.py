from Funciones import LeerNumeros, Promedio

numeros = LeerNumeros(10, "numero")
promedio = Promedio([i for i in numeros if i%2==0])
print(promedio)