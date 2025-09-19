# Matriz de contactos (nombre, teléfono, email)
contactos = [
    ["Juan Pérez", "3123456789", "juan@gmail.com"],
    ["María Gómez", "3156789123", "maria@hotmail.com"],
    ["Carlos Ruiz", "3109876543", "carlos@yahoo.com"]
]

# Guardar en un archivo como texto
with open("Gestión de archivos/Proyecto/Files/contactos.txt", "w", encoding="utf-8") as archivo:
    for contacto in contactos:        
        linea = ",".join(contacto)  # Convertimos la fila en una cadena con comas: Convierte la lista ["Juan Pérez", "3123456789", "juan@gmail.com"] en "Juan Pérez,3123456789,juan@gmail.com".
        archivo.write(linea + "\n")  # Escribimos cada contacto en una línea


# Leer de un archivo de texto

contactos_cargados = []

with open("Gestión de archivos/Proyecto/Files/contactos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        contacto = linea.strip().split(",")  # Eliminar espacios y separar por comas
        contactos_cargados.append(contacto)

print(contactos_cargados)


####################REEMPLAZAR CARACTERES ######################################

texto = "Hola|Mundo|Python"
texto_modificado = texto.replace("|", ",")  # Reemplaza "|" por ","
print(texto_modificado)  # "Hola,Mundo,Python"
