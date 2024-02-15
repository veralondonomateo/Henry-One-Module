class Nodo():
    def __init__(self,dato) -> None:
        self.dato = dato
        self.izq = None
        self.der = None
    
    def inserVal(self,dato):
        if dato < self.dato:
            if self.izq == None:
                self.izq = Nodo(dato)
            else:
                self.izq.inserVal(dato)

        elif dato > self.dato:
            if self.der == None:
                self.der = Nodo(dato)
            else:
                self.der.inserVal(dato)
        else:
            print("Valor repetido")

    def buscarVal(self,dato):
        if self.dato > dato:
            if self.izq:
                return self.izq.buscarVal(dato)
            else:
                False

        elif self.dato < dato:
            if self.der:
                return self.der.buscarVal(dato)
            else:
                return False
        else:
            return True

    def verVal(self):
        print(self.dato)
        if self.der : self.der.verVal()
        if self.izq : self.izq.verVal()





raiz = Nodo(15)
raiz.inserVal(13)
raiz.inserVal(12)
raiz.inserVal(10)
raiz.inserVal(9)
raiz.inserVal(8)
print(raiz.buscarVal(300))