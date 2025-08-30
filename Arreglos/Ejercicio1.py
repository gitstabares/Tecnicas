from Funciones import *

notas = LeerNumeros(10, "nota")
notaMasAlta, notaMasBaja = ValorAltoBajo(notas)
promedioNotas = Promedio(notas)
cantidadNotasSuperioresPromedio = sum([1 for i in notas if i > promedioNotas])
alumnosAprobados = sum([1 for i in notas if i >= 3])
alumnosReprobados = len(notas)-alumnosAprobados
promedioAprobados = Promedio([i for i in notas if i>=3])
promedioReprobados = Promedio([i for i in notas if i<3])

print("La nota mas alta es:", notaMasAlta)
print("La nota mas baja es:", notaMasBaja)
print("El promedio de las notas es:", promedioNotas)
print("El numero de notas superiores al promedio es:", cantidadNotasSuperioresPromedio)
print("El numero de alumnos aprobados es:", alumnosAprobados)
print("El numero de alumnos reprobados es:", alumnosReprobados)
print("La nota promedio de los alumnos aprobados es:", promedioAprobados)
print("La nota promedio de los alumnos reprobados es:", promedioReprobados)
