# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kumpir_uygulama.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 450)
        self.cmb_kumpir_tipi = QtWidgets.QComboBox(Form)
        self.cmb_kumpir_tipi.setGeometry(QtCore.QRect(320, 40, 181, 22))
        self.cmb_kumpir_tipi.setObjectName("cmb_kumpir_tipi")
        self.cmb_kumpir_tipi.addItem("")
        self.cmb_kumpir_tipi.addItem("")
        self.cmb_kumpir_tipi.addItem("")
        self.edt_sonuc = QtWidgets.QLineEdit(Form)
        self.edt_sonuc.setGeometry(QtCore.QRect(20, 360, 651, 20))
        self.edt_sonuc.setObjectName("edt_sonuc")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 210, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cmb_malzeme1 = QtWidgets.QComboBox(Form)
        self.cmb_malzeme1.setGeometry(QtCore.QRect(320, 90, 161, 22))
        self.cmb_malzeme1.setObjectName("cmb_malzeme1")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme2 = QtWidgets.QComboBox(Form)
        self.cmb_malzeme2.setGeometry(QtCore.QRect(320, 130, 161, 22))
        self.cmb_malzeme2.setObjectName("cmb_malzeme2")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_cikolata = QtWidgets.QComboBox(Form)
        self.cmb_cikolata.setGeometry(QtCore.QRect(320, 170, 161, 22))
        self.cmb_cikolata.setObjectName("cmb_cikolata")
        self.cmb_cikolata.addItem("")
        self.cmb_cikolata.addItem("")
        self.cmb_cikolata.addItem("")
        self.cmb_susleme = QtWidgets.QComboBox(Form)
        self.cmb_susleme.setGeometry(QtCore.QRect(320, 210, 161, 22))
        self.cmb_susleme.setObjectName("cmb_susleme")
        self.cmb_susleme.addItem("")
        self.cmb_susleme.addItem("")
        self.cmb_susleme.addItem("")
        self.cmb_susleme.addItem("")
        self.btn_Hesapla = QtWidgets.QPushButton(Form)
        self.btn_Hesapla.setGeometry(QtCore.QRect(280, 290, 141, 23))
        self.btn_Hesapla.setObjectName("btn_Hesapla")
        
        self.cmb_malzeme1.setEnabled(False)
        self.cmb_malzeme2.setEnabled(False)
        self.cmb_cikolata.setEnabled(False)
        self.cmb_susleme.setEnabled(False)
        self.cmb_kumpir_tipi.currentIndexChanged.connect(self.kumpir_tipi_secildi)
        self.btn_Hesapla.clicked.connect(self.btn_Hesapla_clicked)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Express Kumpir Programı"))
        self.cmb_kumpir_tipi.setItemText(0, _translate("Form", "Sade Kumpir: Tereyağ + Kaşar   - 12 TL"))
        self.cmb_kumpir_tipi.setItemText(1, _translate("Form", "Çift Kaşarlı Kumpir    - 17 TL"))
        self.cmb_kumpir_tipi.setItemText(2, _translate("Form", "Karışık Kumpir     - 15 TL"))
        self.label.setText(_translate("Form", "Kumpir Tipi Seçiniz :"))
        self.label_3.setText(_translate("Form", "Kumpir Malzemesi 1 Seçiniz :"))
        self.label_4.setText(_translate("Form", "Çikolata seçiniz :"))
        self.label_5.setText(_translate("Form", "Kumpir Malzemesi 2 Seçiniz :"))
        self.label_6.setText(_translate("Form", "Süsleme Seçiniz :"))
        self.cmb_malzeme1.setItemText(0, _translate("Form", "Mantar"))
        self.cmb_malzeme1.setItemText(1, _translate("Form", "Rus salatası"))
        self.cmb_malzeme1.setItemText(2, _translate("Form", "Siyah zeytin"))
        self.cmb_malzeme1.setItemText(3, _translate("Form", "Yeşil zeytin"))
        self.cmb_malzeme1.setItemText(4, _translate("Form", "Mısır"))
        self.cmb_malzeme1.setItemText(5, _translate("Form", "Bezelye"))
        self.cmb_malzeme1.setItemText(6, _translate("Form", "Turşu"))
        self.cmb_malzeme1.setItemText(7, _translate("Form", "Ketçap"))
        self.cmb_malzeme1.setItemText(8, _translate("Form", "Mayonez"))
        self.cmb_malzeme2.setItemText(0, _translate("Form", "Mantar"))
        self.cmb_malzeme2.setItemText(1, _translate("Form", "Rus salatası"))
        self.cmb_malzeme2.setItemText(2, _translate("Form", "Mısır"))
        self.cmb_malzeme2.setItemText(3, _translate("Form", "Ketçap"))
        self.cmb_malzeme2.setItemText(4, _translate("Form", "Mayonez"))
        self.cmb_malzeme2.setItemText(5, _translate("Form", "Bezelye"))
        self.cmb_malzeme2.setItemText(6, _translate("Form", "Turşu"))
        self.cmb_malzeme2.setItemText(7, _translate("Form", "Siyah zeytin"))
        self.cmb_malzeme2.setItemText(8, _translate("Form", "Yeşil zeytin"))
        self.cmb_cikolata.setItemText(0, _translate("Form", "Beyaz"))
        self.cmb_cikolata.setItemText(1, _translate("Form", "Sütlü"))
        self.cmb_cikolata.setItemText(2, _translate("Form", "Franbuazlı"))
        self.cmb_susleme.setItemText(0, _translate("Form", "Hindistan cevizi"))
        self.cmb_susleme.setItemText(1, _translate("Form", "Damla çikolata"))
        self.cmb_susleme.setItemText(2, _translate("Form", "Muz"))
        self.cmb_susleme.setItemText(3, _translate("Form", "Çilek"))
        self.btn_Hesapla.setText(_translate("Form", "Fiş kes - Hesapla"))


    def kumpir_tipi_secildi(self):
        secilen_index = self.cmb_kumpir_tipi.currentIndex()
        if (secilen_index < 2):
            self.cmb_malzeme1.setEnabled(False)
            self.cmb_malzeme2.setEnabled(False)
            self.cmb_cikolata.setEnabled(False)
            self.cmb_susleme.setEnabled(False)
        else:
            self.cmb_malzeme1.setEnabled(True)
            self.cmb_malzeme2.setEnabled(True)
            self.cmb_cikolata.setEnabled(True)
            self.cmb_susleme.setEnabled(True)


    def btn_Hesapla_clicked(self):
        str_sonuc = ""
        secilen_index = self.cmb_kumpir_tipi.currentIndex()
        if (secilen_index < 2):
            str_sonuc = self.cmb_kumpir_tipi.currentText()
        else:
            str_sonuc = self.cmb_malzeme1.currentText() + ",  " +  \
            self.cmb_malzeme2.currentText() + ",  " + \
            self.cmb_cikolata.currentText() + ",  " + \
            self.cmb_susleme.currentText() + ",  " + \
            self.cmb_kumpir_tipi.currentText()
        
        self.edt_sonuc.setText(str_sonuc)    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

