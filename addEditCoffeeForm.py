# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setObjectName("type_label")
        self.verticalLayout_2.addWidget(self.type_label)
        self.roast_label = QtWidgets.QLabel(self.centralwidget)
        self.roast_label.setObjectName("roast_label")
        self.verticalLayout_2.addWidget(self.roast_label)
        self.texture_label = QtWidgets.QLabel(self.centralwidget)
        self.texture_label.setObjectName("texture_label")
        self.verticalLayout_2.addWidget(self.texture_label)
        self.taste_label = QtWidgets.QLabel(self.centralwidget)
        self.taste_label.setObjectName("taste_label")
        self.verticalLayout_2.addWidget(self.taste_label)
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setObjectName("price_label")
        self.verticalLayout_2.addWidget(self.price_label)
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setObjectName("volume_label")
        self.verticalLayout_2.addWidget(self.volume_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.type = QtWidgets.QLineEdit(self.centralwidget)
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.roast = QtWidgets.QComboBox(self.centralwidget)
        self.roast.setObjectName("roast")
        self.verticalLayout.addWidget(self.roast)
        self.texture = QtWidgets.QComboBox(self.centralwidget)
        self.texture.setObjectName("texture")
        self.verticalLayout.addWidget(self.texture)
        self.taste = QtWidgets.QLineEdit(self.centralwidget)
        self.taste.setObjectName("taste")
        self.verticalLayout.addWidget(self.taste)
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setObjectName("price")
        self.verticalLayout.addWidget(self.price)
        self.volume = QtWidgets.QLineEdit(self.centralwidget)
        self.volume.setObjectName("volume")
        self.verticalLayout.addWidget(self.volume)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout_3.addWidget(self.save_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage"))
        self.type_label.setText(_translate("MainWindow", "название сорта"))
        self.roast_label.setText(_translate("MainWindow", "степень обжарки"))
        self.texture_label.setText(_translate("MainWindow", "молотый/в зернах"))
        self.taste_label.setText(_translate("MainWindow", "описание вкуса"))
        self.price_label.setText(_translate("MainWindow", "цена"))
        self.volume_label.setText(_translate("MainWindow", "объем упаковки"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить"))
