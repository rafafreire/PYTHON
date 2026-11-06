import subprocess

## Creación de nuestro primer script

nombre = "Rafael"
numero = 23
#print ("Esto es nuevo " + str(numero) + "  de " + nombre)

#with open('USUARIOS_HIBERUS.txt', 'r', encoding='utf-8') as archivo:
#    contenido = archivo.read()
#    print(contenido)

with open('./LISTAS/USUARIOS_HIBERUS.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

# for i, linea in enumerate(lineas):
#     if i>=2:
#         #print (lineas [i])
#         print (linea)


# Inicializar listas vacías
partes = []
nombres = []
dnis = []
accesos = []


# Supongamos que el archivo usuarios.txt tiene formato: "Juan Perez,12345678A"
try:
    with open('USUARIOS_HIBERUS.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Separar por coma (o el delimitador que tenga el txt)
            partes = linea.strip().split(',')
            partes_0 = linea[0:34].strip()
            partes_1 = linea[35:44].strip()
            partes_2 = linea[45:90].strip()
            
            if len(partes) == 2:
                nombres.append(partes_0) # Lista 1: Nombres [6]
                dnis.append(partes_1)    # Lista 2: DNI [2]
                accesos.append(partes_2)    # Lista 3: Accesos [3]
except FileNotFoundError:
    print("El archivo no fue encontrado.")

print("Nombres:", nombres)
print("\n\n")
print("DNIs:", dnis)
print("\n\n")
print("Accesos:", accesos)
print("\n\n")

tabla = []

for fila in zip(nombres,dnis):
    tabla.append(list(fila))
print("Tabla creada:\n")


print("Imprimimos la tabla:\n")
for fila in tabla:
    print(fila)

print("\n\nLos usuarios de HIBERUS son los siguientes: ")
print("------------------------------------------\n ")

for fila in tabla:
    print("Usuario: " + fila[0] + " - DNI: " + fila[1])




