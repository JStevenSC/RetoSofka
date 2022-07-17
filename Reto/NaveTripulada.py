from Nave import Nave

class Tripulada(Nave):
    def __init__ (self,nombre,pais,NTripulantes,TipoMision,Orbitableible):

        super().__init__(nombre,pais)
        self.NTripulantes = NTripulantes
        self.TipoMision = TipoMision
        self.Orbitableible = Orbitableible




