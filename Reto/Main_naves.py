import sys
from Principal import *
from Tripuladas   import Ui_Dialog
from NoTripuladas import Ui_Dialog1
from Lanzamiento  import Ui_Dialog2
from PyQt5 import QtCore, QtGui, QtWidgets
from Queries_SQL import Queries_SQL

from NaveLanzamiento import Lanzamiento
from NaveTripulada import Tripulada
from NaveNoTripulada import NoTripulada



import sqlite3

class interfaz(QtWidgets.QMainWindow):

    def __init__(self, parent=None): 

        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##Llamado a ventana tripulante
        self.VentanaTripulada = QtWidgets.QDialog()
        self.ui_Tripulada = Ui_Dialog()
        self.ui_Tripulada.setupUi(self.VentanaTripulada)
       
        ##Llamado a No ventana tripulante
        self.VentanaNoTripulada = QtWidgets.QDialog()
        self.ui_NoTripulada = Ui_Dialog1()
        self.ui_NoTripulada.setupUi(self.VentanaNoTripulada)
        
        ##Llamado a ventana Lanzadora
        self.VentanaLanzamiento = QtWidgets.QDialog()
        self.ui_Lanzamiento = Ui_Dialog2()
        self.ui_Lanzamiento.setupUi(self.VentanaLanzamiento)
        

        #Lectura Botones 
        self.ui.Boton_Lanzamiento.clicked.connect(self.Lanzamientos)
        self.ui.Boton_NTripulada.clicked.connect(self.NoTripuladas)
        self.ui.Boton_Tripulada.clicked.connect(self.Tripuladas)
        #Lectura Botones Lanzadera
        self.ui_Lanzamiento.Agregar_Lanzamiento.clicked.connect(self.insertarLanzador)
        self.ui_Lanzamiento.Consultar_Lanzamiento.clicked.connect(self.consultarLanzador)
        #Lectura Botones Tripulada
        self.ui_Tripulada.Agregar_Tripuladas.clicked.connect(self.insertarTripulada)
        self.ui_Tripulada.Consultar_Tripuladas.clicked.connect(self.consultarTripulada)
        #Lectura Botones No Tripulda
        self.ui_NoTripulada.Agregar_NTripuladas.clicked.connect(self.insertarNoTripulada)
        self.ui_NoTripulada.Consultar_NTripuladas.clicked.connect(self.consultarNoTripulada)



    def Lanzamientos(self):
        self.VentanaLanzamiento.show()
        
    def NoTripuladas(self):
        self.VentanaNoTripulada.show()

    def Tripuladas(self):
        self.VentanaTripulada.show()


    def insertarLanzador(self):

        nombre = str(self.ui_Lanzamiento.tableWidget_4.item(0,0).text())
        pais = str(self.ui_Lanzamiento.tableWidget_4.item(0,1).text())
        CargaUtil = str(self.ui_Lanzamiento.tableWidget_4.item(0,2).text())
        Potencia = str(self.ui_Lanzamiento.tableWidget_4.item(0,3).text())
        Combustible = str(self.ui_Lanzamiento.tableWidget_4.item(0,4).text())
        ##Inserta en Base de datos 
        
        NuevoLanzamiento=Lanzamiento(nombre,pais,CargaUtil,Potencia,Combustible)
        Queries_SQL.InsertarLanzadera(NuevoLanzamiento.nombre,NuevoLanzamiento.pais,NuevoLanzamiento.CargaUtil,NuevoLanzamiento.Potencia,NuevoLanzamiento.Combustible)
        
    
    
    def consultarLanzador(self): 
        respuesta =Queries_SQL.ConsultarLanzadera
        tablerow=0

        for  fila in respuesta():
            print(fila[0])
            
            self.ui_Lanzamiento.tableWidget_3.setItem(tablerow,0,QtWidgets.QTableWidgetItem(fila[1]))
            self.ui_Lanzamiento.tableWidget_3.setItem(tablerow,1,QtWidgets.QTableWidgetItem(fila[2]))
            self.ui_Lanzamiento.tableWidget_3.setItem(tablerow,2,QtWidgets.QTableWidgetItem(fila[3]))
            self.ui_Lanzamiento.tableWidget_3.setItem(tablerow,3,QtWidgets.QTableWidgetItem(fila[4]))
            self.ui_Lanzamiento.tableWidget_3.setItem(tablerow,4,QtWidgets.QTableWidgetItem(fila[5]))
            tablerow += 1

    def insertarTripulada(self):
        
        nombre = str(self.ui_Tripulada.tableWidget_4.item(0,0).text())
        pais = str(self.ui_Tripulada.tableWidget_4.item(0,1).text())
        NoTripulantes = str(self.ui_Tripulada.tableWidget_4.item(0,2).text())
        TipoMision= str(self.ui_Tripulada.tableWidget_4.item(0,3).text())
        Orbita = str(self.ui_Tripulada.tableWidget_4.item(0,4).text())
       
        NuevoTripulada=Tripulada(nombre,pais,NoTripulantes,TipoMision,Orbita)
        ##Inserta en Base de datos 
        Queries_SQL.InsertarTripulada(NuevoTripulada.nombre,NuevoTripulada.pais,NuevoTripulada.NTripulantes,NuevoTripulada.TipoMision,NuevoTripulada.Orbitableible)

            
    def consultarTripulada(self): 
        respuesta =Queries_SQL.ConsultarTripulada
        tablerow=0

        for  fila in respuesta():
            print(fila[0])
            
            self.ui_Tripulada.tableWidget_3.setItem(tablerow,0,QtWidgets.QTableWidgetItem(fila[1]))
            self.ui_Tripulada.tableWidget_3.setItem(tablerow,1,QtWidgets.QTableWidgetItem(fila[2]))
            self.ui_Tripulada.tableWidget_3.setItem(tablerow,2,QtWidgets.QTableWidgetItem(fila[3]))
            self.ui_Tripulada.tableWidget_3.setItem(tablerow,3,QtWidgets.QTableWidgetItem(fila[4]))
            self.ui_Tripulada.tableWidget_3.setItem(tablerow,4,QtWidgets.QTableWidgetItem(fila[5]))
            tablerow += 1

    def insertarNoTripulada(self):
        
        nombre = str(self.ui_NoTripulada.tableWidget_4.item(0,0).text())
        pais = str(self.ui_NoTripulada.tableWidget_4.item(0,1).text())
        Celda = str(self.ui_NoTripulada.tableWidget_4.item(0,2).text())
        NMotores= str(self.ui_NoTripulada.tableWidget_4.item(0,3).text())
        empuje = str(self.ui_NoTripulada.tableWidget_4.item(0,4).text())
       
        NuevoNoTripulada=NoTripulada(nombre,pais,Celda,NMotores,empuje)
        ##Inserta en Base de datos 
        Queries_SQL.InsertarNoTripulada(NuevoNoTripulada.nombre,NuevoNoTripulada.pais,NuevoNoTripulada.Celdas,NuevoNoTripulada.NMotores,NuevoNoTripulada.empuje)

        #print(nombre,pais,Celda,NMotores,empuje)
        #Queries_SQL.InsertarTripulada(NuevoTripulada.nombre,NuevoTripulada.pais,NuevoTripulada.NTripulantes,NuevoTripulada.TipoMision,NuevoTripulada.Orbitableible)

              
    def consultarNoTripulada(self): 
        respuesta =Queries_SQL.ConsultarNoTripulada
        tablerow=0
        print('enyrof')

        for  fila in respuesta():
            print(fila[0])
            
            self.ui_NoTripulada.tableWidget_3.setItem(tablerow,0,QtWidgets.QTableWidgetItem(fila[1]))
            self.ui_NoTripulada.tableWidget_3.setItem(tablerow,1,QtWidgets.QTableWidgetItem(fila[2]))
            self.ui_NoTripulada.tableWidget_3.setItem(tablerow,2,QtWidgets.QTableWidgetItem(fila[3]))
            self.ui_NoTripulada.tableWidget_3.setItem(tablerow,3,QtWidgets.QTableWidgetItem(fila[4]))
            self.ui_NoTripulada.tableWidget_3.setItem(tablerow,4,QtWidgets.QTableWidgetItem(fila[5]))
            tablerow += 1
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    mi_app = interfaz() 
    mi_app.show()
    sys.exit(app.exec_())