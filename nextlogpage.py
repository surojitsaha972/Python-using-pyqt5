# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextlogpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from maindb import *
from updatedb import *

class Ui_insertpage(object):
    def setupUi(self, insertpage):
        insertpage.setObjectName("insertpage")
        insertpage.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(insertpage)
        self.centralwidget.setObjectName("centralwidget")
        insertpage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(insertpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        insertpage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(insertpage)
        self.statusbar.setObjectName("statusbar")
        insertpage.setStatusBar(self.statusbar)
        self.actionInsert = QtWidgets.QAction(insertpage)
        self.actionInsert.setObjectName("actionInsert")
        self.actionUpdate = QtWidgets.QAction(insertpage)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menuMenu.addAction(self.actionInsert)
        self.menuMenu.addAction(self.actionUpdate)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.menubar.triggered[QtWidgets.QAction].connect(self.dis)

        self.retranslateUi(insertpage)
        QtCore.QMetaObject.connectSlotsByName(insertpage)

    def retranslateUi(self, insertpage):
        _translate = QtCore.QCoreApplication.translate
        insertpage.setWindowTitle(_translate("insertpage", "MainWindow"))
        self.menuMenu.setTitle(_translate("insertpage", "Menu"))
        self.actionInsert.setText(_translate("insertpage", "Insert"))
        self.actionUpdate.setText(_translate("insertpage", "Update"))

    def dis(self,action):
        txt = action.text()
        if txt == "Insert":
            self.mainpage = QtWidgets.QMainWindow()
            self.ui = Ui_mainpage()
            self.ui.setupUi(self.mainpage)
            self.mainpage.show()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    insertpage = QtWidgets.QMainWindow()
    ui = Ui_insertpage()
    ui.setupUi(insertpage)
    insertpage.show()
    sys.exit(app.exec_())
