"""
Escribir un programa que pregunte al usuario por las ventas de un rango de años 
y muestre por pantalla una serie con los datos de las ventas indexada por los años, 
antes y después de aplicarles un descuento del 10%.

"""

import pandas as pd
import numpy as np

def ventas_durante_ultimos_4_años(ventas, precio):
    serie_ventas = np.array(ventas)
    dataframe = pd.DataFrame({"Ventas":ventas,"Total sin IVA": list(serie_ventas * precio), "Total menos IVA": list((serie_ventas * precio) - ((serie_ventas*precio) * 0.19))}, index = [i for i in range(2017,2024)])
    print(dataframe)

if __name__ == "__main__":
    ventas = []
    año = 2017
    while año < 2024:
        answer = int(input(f"Cuantas fueron tus ventas durante el año {año} => "))
        año += 1 
        ventas.append(answer)
    precio = int(input("¿Cual es el precio promedio de cada producto? "))
    var = ventas_durante_ultimos_4_años(ventas,precio)
    var.info()


