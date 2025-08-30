def Promedio(n):
    if (len(n) <= 0):
        return 0
    sum = 0
    for i in n:
        sum += i
    return sum/len(n)

def LeerNumeros(n : float,tipoDato : str):
    valores = n*[None]
    i = 0
    while valores[i] == None:
        try:
            valores[i] = float(input(f"Digite su {tipoDato} #{i+1}: "))
            i+=1
        except:
            print("Valor invalido")
        if i >= n:
            break
    return valores

def LeerTexto(n : float, tipoDato : str, permitidos : list = []):
    textos = n*[None]
    i = 0
    while textos[i] == None:
        try:
            textos[i] = input(f"Digite su {tipoDato} #{i+1}: ")
            if textos[i] not in permitidos and len(permitidos) > 0:
                raise Exception
            i+=1
        except:
            textos[i] = None
            print("Valor invalido")
        if i >= n:
            break
    return textos