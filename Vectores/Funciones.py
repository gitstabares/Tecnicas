def Promedio(notas):
    if (len(notas) <= 0):
        return 0
    sum = 0
    for i in notas:
        sum += i
    return sum/len(notas)

def Leer(n : float,tipoDato : str):
    notas = n*[None]
    i = 0
    while notas[i] == None:
        try:
            notas[i] = float(input(f"Digite su {tipoDato} #{i+1}: "))
            i+=1
        except:
            print("Valor invalido")
        if i >= n:
            break
    return notas