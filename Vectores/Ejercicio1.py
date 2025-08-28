def Leer(n):
    notas = n*[None]
    for i in range(n):
        print(f"Digite la nota #{i+1}")
        notas[i] = input()
    return notas

def NotaAltayBaja(notas):
    notaAlta,notaBaja = 2*[notas[0]]
    for i in notas:
        if i > notaAlta:
            notaAlta = i
        if i < notaBaja:
            notaBaja = i
    return notaAlta, notaBaja

def Promedio(notas):
    sum = 0
    for i in notas:
        sum += i
    return sum/len(notas)

notas = Leer(10)
notaMasAlta, notaMasBaja = NotaAltayBaja(notas)
promedioNotas = Promedio(notas)
cantidadNotasSuperioresPromedio = sum([1 for i in notas if i > promedioNotas])
alumnosAprobados = sum([1 for i in notas if i >= 3])
alumnosReprobados = len(notas)-alumnosAprobados
promedioAprobados = Promedio([i for i in notas if i>=3])
promedioReprobados = Promedio([i for i in notas if i<3])