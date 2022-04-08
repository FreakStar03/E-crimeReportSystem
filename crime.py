# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crime_report.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from time import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from datetime import date, datetime#tocopy
import mysql_comn

class Ui_pnl_user(object):
    #pushButton_submitsignal2 = QtCore.pyqtSignal()
    def setupUi(self, pnl_user):
        timer = QtCore.QTimer(pnl_user)#tocopy
        timer.timeout.connect(lambda: self.retranslateUi(pnl_user))#tocopy
        timer.start(1000)#tocopy    
        pnl_user.setObjectName("pnl_user")
        pnl_user.resize(1400, 800)
        pnl_user.setStyleSheet("background: #FFFFFF;\n"
"")
        self.topheader = QtWidgets.QFrame(pnl_user)
        self.topheader.setGeometry(QtCore.QRect(0, 0, 1401, 80))
        self.topheader.setStyleSheet("position: absolute;\n"
"background: #7879FF;\n"
"border-radius: 0px 0px 25px 25px;\n"
"")
        self.topheader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topheader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topheader.setObjectName("topheader")
        self.btnlogout = QtWidgets.QPushButton(self.topheader)
        self.btnlogout.setGeometry(QtCore.QRect(43, 29, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnlogout.setFont(font)
        self.btnlogout.setStyleSheet("color: #F80000;\n"
"")
        self.btnlogout.setObjectName("btnlogout")
        self.pushButton_2 = QtWidgets.QPushButton(self.topheader)
        self.pushButton_2.setGeometry(QtCore.QRect(1230, 30, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: #0000;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.topheader)
        self.label_4.setGeometry(QtCore.QRect(520, 10, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FFFFFF;\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(pnl_user)
        self.label.setGeometry(QtCore.QRect(120, 190, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(pnl_user)
        self.label_2.setGeometry(QtCore.QRect(120, 480, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(pnl_user)
        self.label_3.setGeometry(QtCore.QRect(120, 280, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(pnl_user)
        self.label_5.setGeometry(QtCore.QRect(120, 440, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(pnl_user)
        self.label_6.setGeometry(QtCore.QRect(120, 360, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(pnl_user)
        self.label_7.setGeometry(QtCore.QRect(730, 190, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(pnl_user)
        self.label_8.setGeometry(QtCore.QRect(730, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(pnl_user)
        self.label_9.setGeometry(QtCore.QRect(730, 370, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(pnl_user)
        self.textEdit.setGeometry(QtCore.QRect(290, 280, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(pnl_user)
        self.textEdit_2.setGeometry(QtCore.QRect(290, 370, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(pnl_user)
        self.textEdit_3.setGeometry(QtCore.QRect(290, 450, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(pnl_user)
        self.textEdit_4.setGeometry(QtCore.QRect(880, 190, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(pnl_user)
        self.textEdit_5.setGeometry(QtCore.QRect(890, 370, 361, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton = QtWidgets.QPushButton(pnl_user)
        self.pushButton.setGeometry(QtCore.QRect(640, 690, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("position: absolute;\n"
"background: #7879FF;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(pnl_user)
        self.radioButton.setGeometry(QtCore.QRect(890, 300, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(pnl_user)
        self.radioButton_2.setGeometry(QtCore.QRect(990, 300, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(pnl_user)
        self.radioButton_3.setGeometry(QtCore.QRect(1120, 300, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.textEdit_6 = QtWidgets.QTextEdit(pnl_user)
        self.textEdit_6.setGeometry(QtCore.QRect(290, 190, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.checkBox = QtWidgets.QCheckBox(pnl_user)
        self.checkBox.setGeometry(QtCore.QRect(140, 590, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(pnl_user)
        QtCore.QMetaObject.connectSlotsByName(pnl_user)

    def retranslateUi(self, pnl_user):
        now = datetime.now()#tocopy
        _translate = QtCore.QCoreApplication.translate
        pnl_user.setWindowTitle(_translate("pnl_user", "Dialog"))
        self.btnlogout.setText(_translate("pnl_user", "Back"))
        self.pushButton_2.setText(_translate("pnl_user",  now.strftime("%H:%M:%S"))) #tocopy
        self.label_4.setText(_translate("pnl_user", "Crime Reporting"))
        self.label.setText(_translate("pnl_user", "Crime Date :"))
        self.label_2.setText(_translate("pnl_user", "Overview :"))
        self.label_3.setText(_translate("pnl_user", "Crime Time :"))
        self.label_5.setText(_translate("pnl_user", "Criminal "))
        self.label_6.setText(_translate("pnl_user", "Crime Type :"))
        self.label_7.setText(_translate("pnl_user", "Location :"))
        self.label_8.setText(_translate("pnl_user", "Gender :"))
        self.label_9.setText(_translate("pnl_user", "Description :"))
        self.pushButton.setText(_translate("pnl_user", "SUBMIT"))
        self.radioButton.setText(_translate("pnl_user", "Male"))
        self.radioButton_2.setText(_translate("pnl_user", "Female"))
        self.radioButton_3.setText(_translate("pnl_user", "Transgender"))
        self.checkBox.setText(_translate("pnl_user", "This details are currect.This details can\'t Be changes.I have suffer from this crime."))
        self.pushButton.clicked.connect(self.report)
    def checkgender(self):
        if self.radioButton.isChecked()    : return self.radioButton.text()
        if self.radioButton_2.isChecked() : return self.radioButton_2.text()
        if self.radioButton_3.isChecked() : return self.radioButton_3.text()
        return "hello"
    
    def report(self):
        date1 = self.textEdit_6.toPlainText()
        time1 = self.textEdit.toPlainText()
        type1 = self.textEdit_2.toPlainText()
        overview = self.textEdit_3.toPlainText()
        location = self.textEdit_4.toPlainText()
        gender = self.checkgender()
        description = self.textEdit_5.toPlainText()
        checkbox= self.checkBox.isChecked()
        isvalid=True
                
        if all((len(date1),checkbox, len(time1), len(type1), len(overview),len(location),len(gender),len(description))):
                try:
                        mydb = mysql_comn.mydb
                        mycursor = mydb.cursor()
                        
                        AmountOfRow = mycursor.rowcount
                        sql = "INSERT INTO crimereport (`Date`,`Time`,`Type`,`Overview`,`Location`,`Gender`,`Description`) VALUES (%s, %s,%s, %s,%s, %s,%s)"
                        val = (date1, time1,type1,overview,location,gender,description)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        
                        if(AmountOfRow == mycursor.rowcount):
                                print("ERROR")
                        else:
                                print("ADDED")
                        
                        msg = QMessageBox()
                        msg.setWindowTitle("Registration Form")
                        msg.setText("Registration Successfull")
                        msg.exec_()
                        self.pushButton_submitsignal2.emit()
                except mysql.connector.Error as err:
                        
                        print(err)
        
        
        
if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   Dialog = QtWidgets.QWidget()
   ui = Ui_pnl_user()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())
        
        