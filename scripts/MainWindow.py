# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 270, 641, 230))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkWrite = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkWrite.setObjectName("checkWrite")
        self.gridLayout.addWidget(self.checkWrite, 5, 1, 1, 1)
        self.checkFFT = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkFFT.setChecked(True)
        self.checkFFT.setObjectName("checkFFT")
        self.gridLayout.addWidget(self.checkFFT, 4, 1, 1, 1)
        self.btnStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnStop.setPalette(palette)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 6, 2, 1, 1)
        self.checkSub = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkSub.setObjectName("checkSub")
        self.gridLayout.addWidget(self.checkSub, 4, 0, 1, 1)
        self.spinLower = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinLower.setMaximum(10000)
        self.spinLower.setObjectName("spinLower")
        self.gridLayout.addWidget(self.spinLower, 1, 1, 1, 1)
        self.btnStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 249, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 249, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 249, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnStart.setPalette(palette)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 6, 1, 1, 1)
        self.btnSaveSpec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSaveSpec.setObjectName("btnSaveSpec")
        self.gridLayout.addWidget(self.btnSaveSpec, 7, 1, 1, 1)
        self.btnTakeRef = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnTakeRef.setObjectName("btnTakeRef")
        self.gridLayout.addWidget(self.btnTakeRef, 6, 0, 1, 1)
        self.btnLoadRef = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnLoadRef.setObjectName("btnLoadRef")
        self.gridLayout.addWidget(self.btnLoadRef, 2, 0, 1, 1)
        self.btnShowRef = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnShowRef.setObjectName("btnShowRef")
        self.gridLayout.addWidget(self.btnShowRef, 5, 0, 1, 1)
        self.spinUpper = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinUpper.setMaximum(10000)
        self.spinUpper.setObjectName("spinUpper")
        self.gridLayout.addWidget(self.spinUpper, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuSpecra_Viewer = QtWidgets.QMenu(self.menubar)
        self.menuSpecra_Viewer.setObjectName("menuSpecra_Viewer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSpecra_Viewer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkWrite.setText(_translate("MainWindow", "Write to Files"))
        self.checkFFT.setText(_translate("MainWindow", "Show Fouriertransform"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.checkSub.setText(_translate("MainWindow", "Substract Reference"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnSaveSpec.setText(_translate("MainWindow", "Save current Spectra"))
        self.btnTakeRef.setText(_translate("MainWindow", "Take Reference"))
        self.btnLoadRef.setText(_translate("MainWindow", "Load Reference from File"))
        self.btnShowRef.setText(_translate("MainWindow", "Show Reference spectra"))
        self.label.setText(_translate("MainWindow", "Spectrum Upperbound"))
        self.label_2.setText(_translate("MainWindow", "Spectrum Lowerbound"))
        self.menuSpecra_Viewer.setTitle(_translate("MainWindow", "Specra-Viewer"))
        #Buttons
        
        
        
