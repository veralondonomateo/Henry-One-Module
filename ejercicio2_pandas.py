"""
Escribir una función que reciba 
un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima,
la máxima, media y la desviación típica.

"""

import pandas as pd

#Funcion
def notas(diccionario):
    dict = pd.DataFrame(diccionario)
    dict2 = dict.loc[dict["Notas"].idxmin()] #Mínima nota
    dict3 = dict.loc[dict["Notas"].idxmax()] #Máxima nota
    serie1 =  pd.Series(list(dict2),index = ["Nombre", "Nota"] ) #Serie min
    serie2 =  pd.Series(list(dict3), index = ["Nombre", "Nota"]) #Serie max
    media = dict["Notas"].mean() #Media
    std = dict["Notas"].std() #Estandar desvition

    return f'El estudiante con menor nota es: \n{serie1} \n \nEl estudiante con mejor nota es:\n{serie2} \nLa media de las notas es: {media}'



if __name__ == "__main__":
    
    nombres = []
    notass = []
    diccionario = {"Estudiantes": nombres, "Notas": notass }

    estudiantes = int(input("Cuantos estudiantes son => "))
    for _ in range(estudiantes):
        nombre = input(f"Nombre el estudiante numero {_ + 1} => ")
        nota = float(input("Ingrese la nota del estudiante => "))
        nombres.append(nombre)
        notass.append(nota)

    print(notas(diccionario))





