import csv
archivo = open("/Users/mateovera/Documents/Programación/HENRY/hospitales2.csv",encoding="utf-8")
tabla = csv.reader(archivo, delimiter= ",")
with open("hospitales_salida.csv", "w",encoding="utf-8") as salida: #Estamos creando un nuevo csv
    salida_writer = csv.writer(salida, delimiter= ",")
    next(tabla)
    salida_writer.writerow(["latitude","longitude", "name", "label"])

    for linea in tabla:
        coordenada = linea[0][7:-1].split()
        salida_writer.writerow([coordenada[1],coordenada[0],linea[8],linea[3]])
archivo.close()