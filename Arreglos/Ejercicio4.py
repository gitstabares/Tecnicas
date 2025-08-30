from Funciones import *

nombre = LeerTexto(10,"nombre")
edad = LeerNumeros(10,"edad")
altura = LeerNumeros(10,"altura del estudiante")
mayorEdad,_=ValorAltoBajo(edad)
for i in range(len(edad)):
    if (mayorEdad == edad[i]):
        break
print("El alumno ",nombre[i]," tiene ",edad[i]," años, mide ",altura[i]," y es el alumno con mayor edad")
promedioAltura = Promedio([altura[i] for i in range(len(altura)) if edad[i] >= 18])
promedioEdad = Promedio([i for i in edad if i >= 18])
alumnosAltos =  sum([1 for i in altura if i>= 1.75])
print("La media en la altura de los alumnos mayores de edad es: ", promedioAltura)
print("La media de edad entre los alumnos mayores de edad es: ", promedioEdad)
print("La cantidad de alumnos que miden 1.75 o más es: ", alumnosAltos)