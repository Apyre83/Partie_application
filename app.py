# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory


#TODO: supprimer une tache quand on la coche

class TaskLineWidget(QtWidgets.QWidget):
    """widget créé quand on ajoute une tache (Label+checkbox)"""
    def __init__(self, text ,parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.text = text
        self.lay = QtWidgets.QHBoxLayout(self)
        self.label = QtWidgets.QLabel(text)
        self.button = QtWidgets.QCheckBox()
        self.lay.addWidget(self.label)
        self.lay.addWidget(self.button)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        "création de la fenêtre et de principaux élément graphique"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 600)
        MainWindow.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 721, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(lambda: self.addNewItem()) #permet d'affecter la fonction addNewItem au bouton
                                                                   #(quand on clique dessus)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """à ignorer"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Task :"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))

    def addNewItem(self):
        """fonction exécuter quand on appuie sur le bouton:
        création d'une nouvelle ligne avec le widget 'TaskLineWidget' créé plus haut"""
        if self.lineEdit.text(): #on vérifie que l'utilisateur à écrit du texte
            Item = QtWidgets.QListWidgetItem(self.listWidget)
            Item_Widget = TaskLineWidget(self.lineEdit.text())
            self.lineEdit.clear()
            Item.setSizeHint(Item_Widget.sizeHint())
            self.listWidget.addItem(Item)
            self.listWidget.setItemWidget(Item, Item_Widget)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setStyle(QStyleFactory.create('Fusion'))
    MainWindow.show()
    sys.exit(app.exec_())
