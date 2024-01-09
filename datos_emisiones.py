import os

def abrir_Archivo(archivo):

    dicc_emisiones = {  'cod_pais' : [],
                        'nom_pais' : [],
                        'region' : [],
                        'anio' : [],
                        'co2' : [],
                        'co2_percapita' : []}
        
    encabezado = 0 
    for dato in archivo:
        if encabezado >= 1: 
            archivo = dato.split(sep="|")
            dicc_emisiones['cod_pais'].append(archivo[0])
            dicc_emisiones['nom_pais'].append(archivo[1])
            dicc_emisiones['region'].append(archivo[2])
            dicc_emisiones['anio'].append(archivo[3])
            dicc_emisiones['co2'].append(archivo[4])
            dicc_emisiones['co2_percapita'].append(archivo[5])
        else:
            encabezado += 1

    #Cuanto fueron las emisiones de Co2 en america latina 
        #Durante el año 2010

    region = "América Latina y Caribe"        
    año = "2010"

    indices = []
    for indice,variable in enumerate(dicc_emisiones["region"]):
        if variable == region:
            if dicc_emisiones["anio"][indice] == año:
                if dicc_emisiones['co2'][indice] != "":
                    indices.append(indice)

    co2 = 0
    for i in indices:
        numero = dicc_emisiones['co2'][i]
        numero = numero.replace(",","")
        co2 += round(float(numero),2)

    print(f'En {region} durante el año {año} las emisiones fueron {round(co2,2)} tk')

if __name__ == "__main__":
    abrir_Archivo(open('Emisiones_CO2.csv', 'r', encoding='latin-1'))