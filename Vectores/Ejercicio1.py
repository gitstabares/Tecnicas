from Funciones import LeerNumeros, Promedio

def NotaAltayBaja(notas):
    notaAlta,notaBaja = 2*[notas[0]]
    for i in notas:
        if i > notaAlta:
            notaAlta = i
        if i < notaBaja:
            notaBaja = i
    return notaAlta, notaBaja

notas = LeerNumeros(10, "nota")
notaMasAlta, notaMasBaja = NotaAltayBaja(notas)
promedioNotas = Promedio(notas)
cantidadNotasSuperioresPromedio = sum([1 for i in notas if i > promedioNotas])
alumnosAprobados = sum([1 for i in notas if i >= 3])
alumnosReprobados = len(notas)-alumnosAprobados
promedioAprobados = Promedio([i for i in notas if i>=3])
promedioReprobados = Promedio([i for i in notas if i<3])