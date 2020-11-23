import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Examen.ui",self)
        self.Boton_Grabar.clicked.connect(self.guardar)

    def guardar(self):
        i0= str(self.val0.toPlainText())
        i1= int(self.val1.toPlainText())
        i2= int(self.val2.toPlainText())
        result=[(i0,i1,i2)]
        self.tableWidget.clearContents()
        row = 0
        for endian in result:
            self.tableWidget.setRowCount(row + 1)
            idDato = QTableWidgetItem(endian[0])
            idDato.setTextAlignment(4)
            self.tableWidget.setItem(row, 0, idDato)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(endian[1])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(endian[2])))
            row+= 1
        #Limpiar
        for line in [self.val0, self.val1,self.val2]: line.clear()
        for box in [self.cBoxSi,self.cBoxNo]:box.setChecked(False)

app=QApplication(sys.argv)
dialogo = Ui_Dialog()
dialogo.show()
app.exec_()