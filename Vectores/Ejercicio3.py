from Funciones import LeerTexto,LeerNumeros, Promedio

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
porcentajeHombresTrabajan = 0
porcentajeMujeresTrabajan = 0
if hombres > 0:
    porcentajeHombresTrabajan = hombresTrabajan/hombres*100
if mujeres > 0:
    porcentajeMujeresTrabajan = mujeresTrabajan/mujeres*100
sueldoPromedioHombres = Promedio([sueldo[i] for i in range(personas) if sexo[i] == "m" and trabajo[i] ==1])
sueldoPromedioMujeres = Promedio([sueldo[i] for i in range(personas) if sexo[i] == "f" and trabajo[i] ==1])

print(porcentajeHombres,porcentajeHombresTrabajan,porcentajeMujeres,porcentajeMujeresTrabajan,sueldoPromedioHombres,sueldoPromedioMujeres)