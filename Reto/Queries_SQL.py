from datetime import datetime
from CNXN_SQL import CNXN_SQL_Manager


class Queries_SQL_Class:
    def InsertarLanzadera(self,nombre,pais,CargaUtil,Potencia,Combustible):
        with CNXN_SQL_Manager() as CNXN_SQL:
                   
            CNXN_SQL.Cursor.execute('INSERT INTO Lanzadera(Nombre, Pais ,CargaUtil, PotenciPropulcion, Combustible) VALUES (?,?,?,?,?)' ,(nombre,pais,CargaUtil,Potencia,Combustible))
            CNXN_SQL.Cnxn.commit()

    def ConsultarLanzadera(self):
        with CNXN_SQL_Manager() as CNXN_SQL:
            CNXN_SQL.Cursor.execute("SELECT * FROM Lanzadera")
            Row_Response = CNXN_SQL.Cursor.fetchall()
            return Row_Response

    def InsertarTripulada(self,nombre,pais,NoTripulantes,TipoMision,Orbita):
        with CNXN_SQL_Manager() as CNXN_SQL:
                   
            CNXN_SQL.Cursor.execute('INSERT INTO Tripulada(Nombre, Pais, NoTripulantes,  TipoMision, Orbita) VALUES (?,?,?,?,?)' ,(nombre,pais,NoTripulantes,TipoMision,Orbita))
            CNXN_SQL.Cnxn.commit()

    def ConsultarTripulada(self):
        with CNXN_SQL_Manager() as CNXN_SQL:
            CNXN_SQL.Cursor.execute("SELECT * FROM Tripulada")
            Row_Response = CNXN_SQL.Cursor.fetchall()
            return Row_Response

    def InsertarNoTripulada(self,nombre,pais,Celda,NMotores,empuje):
        with CNXN_SQL_Manager() as CNXN_SQL:
                   
            CNXN_SQL.Cursor.execute('INSERT INTO NoTripulada(Nombre, Pais,CeldaFotovoltaica,NumeroMotores,Empuje) VALUES (?,?,?,?,?)' ,(nombre,pais,Celda,NMotores,empuje))
            CNXN_SQL.Cnxn.commit()

    def ConsultarNoTripulada(self):
        with CNXN_SQL_Manager() as CNXN_SQL:
            CNXN_SQL.Cursor.execute("SELECT * FROM NoTripulada")
            Row_Response = CNXN_SQL.Cursor.fetchall()
            return Row_Response
    





Queries_SQL=Queries_SQL_Class()
            
