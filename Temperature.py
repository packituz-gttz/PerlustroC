# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Temperature.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/:/MainIcon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plotzone = PlotWidget(self.centralwidget)
        self.plotzone.setObjectName(_fromUtf8("plotzone"))
        self.horizontalLayout.addWidget(self.plotzone)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(25, -1, 10, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_temp = QtGui.QLabel(self.centralwidget)
        self.label_temp.setStyleSheet(_fromUtf8("color: blue;\n"
"font: 36pt \"Noto Sans\";"))
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setWordWrap(True)
        self.label_temp.setObjectName(_fromUtf8("label_temp"))
        self.gridLayout.addWidget(self.label_temp, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.checkbox_sound = QtGui.QCheckBox(self.centralwidget)
        self.checkbox_sound.setText(_fromUtf8(""))
        self.checkbox_sound.setObjectName(_fromUtf8("checkbox_sound"))
        self.gridLayout.addWidget(self.checkbox_sound, 2, 1, 1, 1)
        self.pinbox_alert = QtGui.QSpinBox(self.centralwidget)
        self.pinbox_alert.setObjectName(_fromUtf8("pinbox_alert"))
        self.gridLayout.addWidget(self.pinbox_alert, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.button_start = QtGui.QPushButton(self.centralwidget)
        self.button_start.setObjectName(_fromUtf8("button_start"))
        self.verticalLayout.addWidget(self.button_start)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSettings = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/:/Settings")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionInfo = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/:/Info")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInfo.setIcon(icon2)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionReload = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/:/Reload")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReload.setIcon(icon3)
        self.actionReload.setObjectName(_fromUtf8("actionReload"))
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionInfo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionReload)
        self.label_2.setBuddy(self.pinbox_alert)
        self.label_3.setBuddy(self.checkbox_sound)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_temp.setText(_translate("MainWindow", "None", None))
        self.label_2.setText(_translate("MainWindow", "Max &Temperature Alert:", None))
        self.label_3.setText(_translate("MainWindow", "Sound &Warning:", None))
        self.button_start.setText(_translate("MainWindow", "&Start", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionSettings.setToolTip(_translate("MainWindow", "Settings", None))
        self.actionInfo.setText(_translate("MainWindow", "Info", None))
        self.actionInfo.setToolTip(_translate("MainWindow", "Information", None))
        self.actionReload.setText(_translate("MainWindow", "Reload", None))
        self.actionReload.setToolTip(_translate("MainWindow", "Reload", None))

from pyqtgraph import PlotWidget
import perlustroC_resources_rc
