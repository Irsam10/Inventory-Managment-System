# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddAmount.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addAmountWindow(object):
    def setupUi(self, addAmountWindow):
        addAmountWindow.setObjectName("addAmountWindow")
        addAmountWindow.resize(688, 334)
        addAmountWindow.setMaximumSize(QtCore.QSize(688, 334))
        self.centralwidget = QtWidgets.QWidget(addAmountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(220, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.enteredAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.enteredAmount.setGeometry(QtCore.QRect(150, 120, 411, 31))
        self.enteredAmount.setText("")
        self.enteredAmount.setObjectName("enteredAmount")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(270, 170, 121, 31))
        self.addBtn.setObjectName("addBtn")
        self.enterAmountLabel = QtWidgets.QLabel(self.centralwidget)
        self.enterAmountLabel.setGeometry(QtCore.QRect(60, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enterAmountLabel.setFont(font)
        self.enterAmountLabel.setObjectName("enterAmountLabel")
        addAmountWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addAmountWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        addAmountWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addAmountWindow)
        self.statusbar.setObjectName("statusbar")
        addAmountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(addAmountWindow)
        QtCore.QMetaObject.connectSlotsByName(addAmountWindow)

    def retranslateUi(self, addAmountWindow):
        _translate = QtCore.QCoreApplication.translate
        addAmountWindow.setWindowTitle(_translate("addAmountWindow", "Add"))
        self.titleLabel.setText(_translate("addAmountWindow", "Add Amount To product"))
        self.addBtn.setText(_translate("addAmountWindow", "Add"))
        self.enterAmountLabel.setText(_translate("addAmountWindow", "Enter Amount:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addAmountWindow = QtWidgets.QMainWindow()
    ui = Ui_addAmountWindow()
    ui.setupUi(addAmountWindow)
    addAmountWindow.show()
    sys.exit(app.exec_())