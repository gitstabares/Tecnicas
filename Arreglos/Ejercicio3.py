from Funciones import *

personas = 10
sexo = LeerTexto(personas,"sexo (m/f)",list("mf"))
trabajo = LeerNumeros(personas,"trabajo (1. Si trabaja, 2. No trabaja)")
sueldo = LeerNumeros(personas, "sueldo (0 si no trabaja)")
hombres = mujeres = hombresTrabajan = mujeresTrabajan = 0

for i in range(personas):
    if sexo[i] == "m":
        hombres += 1
        if trabajo[i] == 1:
            hombresTrabajan += 1
    elif sexo[i] == "f":
        mujeres += 1
        if trabajo[i] == 1:
            mujeresTrabajan += 1
porcentajeHombres = hombres/personas*100
porcentajeMujeres = mujeres/personas*100
if hombres > 0:
    porcentajeHombresTrabajan = hombresTrabajan/hombres*100
else:
    porcentajeHombresTrabajan = 0
if mujeres > 0:
    porcentajeMujeresTrabajan = mujeresTrabajan/mujeres*100
else:
    porcentajeMujeresTrabajan = 0
sueldoPromedioHombres = Promedio([sueldo[i] for i in range(personas) if sexo[i] == "m" and trabajo[i] ==1])
sueldoPromedioMujeres = Promedio([sueldo[i] for i in range(personas) if sexo[i] == "f" and trabajo[i] ==1])

print("El porcentaje de hombres es:", porcentajeHombres)
print("El porcentaje de mujeres es:", porcentajeMujeres)
print("El porcentaje de hombres que trabajan es:", porcentajeHombresTrabajan)
print("El porcentaje de mujeres que trabajan es:", porcentajeMujeresTrabajan)
print("El sueldo promedio de hombres que trabajan es:", sueldoPromedioHombres)
print("El sueldo promedio de mujeres que trabajan es:", sueldoPromedioMujeres)