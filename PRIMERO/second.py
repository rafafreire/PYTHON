with open('./../../../OPOSICIONES/GSI/EXAMENES/PREGUNTAS_EXAMEN_GSI.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

for i, linea in enumerate(lineas):
    if linea != "" and not("EXAMEN" in linea):
        #print (lineas [i])
        #print ("Linea: " + str(i) + " " + linea)
        print ( linea)
        if ("d)" in linea):
            print("\n")





