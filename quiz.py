# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(920, 221)
        self.edt_mesaj = QtWidgets.QLineEdit(Dialog)
        self.edt_mesaj.setGeometry(QtCore.QRect(50, 50, 311, 20))
        self.edt_mesaj.setObjectName("edt_mesaj")
        self.btn_buyukharf_yap = QtWidgets.QPushButton(Dialog)
        self.btn_buyukharf_yap.setGeometry(QtCore.QRect(390, 50, 131, 23))
        self.btn_buyukharf_yap.setObjectName("btn_buyukharf_yap")
        self.edt_sonuc = QtWidgets.QLineEdit(Dialog)
        self.edt_sonuc.setGeometry(QtCore.QRect(550, 50, 321, 20))
        self.edt_sonuc.setObjectName("edt_sonuc")
        self.btn_karakter_hesapla = QtWidgets.QPushButton(Dialog)
        self.btn_karakter_hesapla.setGeometry(QtCore.QRect(390, 100, 131, 23))
        self.btn_karakter_hesapla.setObjectName("karakter_hesapla")
        
        
        self.btn_buyukharf_yap.clicked.connect(self.btn_buyukharf_yap_clicked)
        self.btn_karakter_hesapla.clicked.connect(self.btn_karakter_hesapla_clicked)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Merhaba"))
        self.btn_buyukharf_yap.setText(_translate("Dialog", "Büyük Harfe Dönüştür"))
        self.btn_karakter_hesapla.setText(_translate("Dialog", "Karakter sayısını bul"))

    def btn_buyukharf_yap_clicked(self):
        msj = self.edt_mesaj.text()
        yeni_msj = msj.upper()
        self.edt_sonuc.setText(yeni_msj)
        
    def btn_karakter_hesapla_clicked(self):
        msj = self.edt_mesaj.text()
        yeni_msj = str(len(msj))
        self.edt_sonuc.setText(yeni_msj)
        
  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

