"""Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L. Las opciones posibles son:

Llenar la jarra de 3 litros
Llenar la jarra de 5 litros
Vaciar la jarra de 3 litros
Vaciar la jarra de 5 litros
Verter el contenido de la jarra de 3 litros en la de 5 litros
Verter el contenido de la jarra de 5 litros en la de 3 litros"""

class Juego:
    def __init__(self) -> None:
        self.jarra3 = 0
        self.jarra5 = 0

    def llenar(self,opcion):
        if opcion == 3:
            self.jarra3 += 3
        elif opcion == 5:
            self.jarra5 += 5

    def vaciar(self,opcion):
        if opcion == 3:
            if self.jarra3 > 0:
                self.jarra3 -= self.jarra3
            else:
                print('El recipiente 3 esta vacio')
        elif opcion == 5:
            if self.jarra5 > 0:
                self.jarra5 -= self.jarra5
            else:
                print('El recipiente 5 esta vacio')

    def consultar(self):
        print(f'En la jarra 3 hay {self.jarra3} lt y en la jarra 5 hay {self.jarra5} lt')

    def cambiar_valores(self,opcion):
        if opcion == 1:
            if self.jarra3 > 0:
                while self.jarra5 < 5 and self.jarra3 > 0:
                    self.jarra5 += 1
                    self.jarra3 -= 1
            else:
                print('La jarra 3 esta vacia')

        elif opcion == 2:
            if self.jarra5 > 0:
                while self.jarra3 < 3 and self.jarra5 > 0:
                    self.jarra3 += 1
                    self.jarra5 -= 1
            else:
                print('La jarra 5 esta vacia')

def main():
    print(('\nJuego de las jarras').upper())
    print('Tienes una jarra de 5 lt y otra de 3 lt')
    print('Como harías para conseguir medir exactamente 4 litros \n')
    intentos = 11
    objeto = Juego()
    while intentos > 0 and objeto.jarra5 != 4:
        print('\nEstas son las opciones. Tienes 5 intentos')
        print("""1 - Llenar la jarra de 3 litros
    2 - Llenar la jarra de 5 litros
    3 - Vaciar la jarra de 3 litros
    4 - Vaciar la jarra de 5 litros
    5 - Verter el contenido de la jarra de 3 litros en la de 5 litros
    6 - Verter el contenido de la jarra de 5 litros en la de 3 litros""")
        
        eleccion = int(input('Pon el número de tu eleccion ==> '))
        if eleccion == 1:
            objeto.llenar(3)
        elif eleccion == 2:
            objeto.llenar(5)
        elif eleccion == 3:
            objeto.vaciar(3)
        elif eleccion == 4:
            objeto.vaciar(5)
        elif eleccion == 5:
            objeto.cambiar_valores(1)
        elif eleccion == 6:
            objeto.cambiar_valores(2)
        else:
            print("Opción no valida")
        print('\n',("*" * 20) )
        objeto.consultar()

        intentos -= 1

    if objeto.jarra5 == 4:
        print('Felicidades, ganaste')
    else:
        print('Perdiste :(')






if __name__ == "__main__":
    main()
        
