# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 180, 671, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 0, 23))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnStop.setPalette(palette)
        self.btnStop.setStyleSheet("background-color: rgb(239, 0, 23);")
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 10, 3, 1, 1)
        self.checkFFT = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkFFT.setChecked(True)
        self.checkFFT.setObjectName("checkFFT")
        self.gridLayout.addWidget(self.checkFFT, 7, 2, 1, 1)
        self.checkWrite = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkWrite.setObjectName("checkWrite")
        self.gridLayout.addWidget(self.checkWrite, 8, 2, 1, 1)
        self.btnTakeRef = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnTakeRef.setStyleSheet("background-color: rgb(212, 199, 0);")
        self.btnTakeRef.setObjectName("btnTakeRef")
        self.gridLayout.addWidget(self.btnTakeRef, 10, 0, 1, 1)
        self.btnSaveSpec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSaveSpec.setStyleSheet("background-color: rgb(79, 145, 255);")
        self.btnSaveSpec.setObjectName("btnSaveSpec")
        self.gridLayout.addWidget(self.btnSaveSpec, 11, 2, 1, 1)
        self.btnStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnStart.setPalette(palette)
        self.btnStart.setStyleSheet("background-color: rgb(0, 226, 0);")
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 10, 2, 1, 1)
        self.btnLoadRef = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnLoadRef.setObjectName("btnLoadRef")
        self.gridLayout.addWidget(self.btnLoadRef, 5, 0, 1, 1)
        self.btnShowRef = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnShowRef.setObjectName("btnShowRef")
        self.gridLayout.addWidget(self.btnShowRef, 7, 0, 1, 1)
        self.checkSub = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkSub.setObjectName("checkSub")
        self.gridLayout.addWidget(self.checkSub, 8, 0, 1, 1)
        self.spinAverage = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinAverage.setMaximum(20)
        self.spinAverage.setObjectName("spinAverage")
        self.gridLayout.addWidget(self.spinAverage, 1, 3, 1, 1)
        self.spinLower = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinLower.setMaximum(10000)
        self.spinLower.setObjectName("spinLower")
        self.gridLayout.addWidget(self.spinLower, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)
        self.checkAverage = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkAverage.setObjectName("checkAverage")
        self.gridLayout.addWidget(self.checkAverage, 1, 2, 1, 1)
        self.spinUpper = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinUpper.setMaximum(10000)
        self.spinUpper.setObjectName("spinUpper")
        self.gridLayout.addWidget(self.spinUpper, 2, 3, 1, 1)
        self.spinInt = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinInt.setMaximum(1000000)
        self.spinInt.setProperty("value", 10000)
        self.spinInt.setObjectName("spinInt")
        self.gridLayout.addWidget(self.spinInt, 5, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 24))
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
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.checkFFT.setText(_translate("MainWindow", "Show Fouriertransform"))
        self.checkWrite.setText(_translate("MainWindow", "Write to Files"))
        self.btnTakeRef.setText(_translate("MainWindow", "Take Reference"))
        self.btnSaveSpec.setText(_translate("MainWindow", "Save current Spectra"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnLoadRef.setText(_translate("MainWindow", "Load Reference from File"))
        self.btnShowRef.setText(_translate("MainWindow", "Show Reference spectra"))
        self.checkSub.setText(_translate("MainWindow", "Substract Reference"))
        self.label_2.setText(_translate("MainWindow", "Spectrum Lowerbound"))
        self.label.setText(_translate("MainWindow", "Spectrum Upperbound"))
        self.checkAverage.setText(_translate("MainWindow", "Average over:"))
        self.label_3.setText(_translate("MainWindow", "Integration time"))
        self.menuSpecra_Viewer.setTitle(_translate("MainWindow", "Specra-Viewer"))
#hahhhh