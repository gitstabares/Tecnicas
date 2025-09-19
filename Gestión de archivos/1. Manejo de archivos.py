

##################### EJERCICIO #6 #######################################
print("\n")
print("EJERCICIO #6")
#Leer y escribir al mismo tiempo ("r+")

with open("Gestión de archivos/Proyecto/Files/archivo.txt", "r+", encoding="utf-8") as archivo: 
    # Al intententar escribir antes de leer se sobreescribe el documento
    archivo.write("Linea previa")
    contenido = archivo.read()
    print("******")
    print(contenido)
    print("******")
    archivo.write("\nNueva línea agregada 123")
    archivo.close()