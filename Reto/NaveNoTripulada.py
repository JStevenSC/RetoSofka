from Nave import Nave

class NoTripulada(Nave):
    def __init__ (self,nombre,pais,Celdas,NMotores,empuje):

        super().__init__(nombre,pais)
        self.Celdas = Celdas
        self.NMotores = NMotores
        self.empuje = empuje
