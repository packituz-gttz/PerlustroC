# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAbout.ui'
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

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName(_fromUtf8("DialogAbout"))
        DialogAbout.resize(501, 317)
        self.label_image = QtGui.QLabel(DialogAbout)
        self.label_image.setGeometry(QtCore.QRect(60, 110, 71, 71))
        self.label_image.setText(_fromUtf8(""))
        self.label_image.setPixmap(QtGui.QPixmap(_fromUtf8(":/:/MainIcon")))
        self.label_image.setObjectName(_fromUtf8("label_image"))
        self.label_2 = QtGui.QLabel(DialogAbout)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 121, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DialogAbout)
        self.label_3.setGeometry(QtCore.QRect(160, 110, 291, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(DialogAbout)
        self.label_4.setGeometry(QtCore.QRect(160, 220, 281, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(DialogAbout)
        self.label_5.setGeometry(QtCore.QRect(160, 170, 211, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_version = QtGui.QLabel(DialogAbout)
        self.label_version.setGeometry(QtCore.QRect(160, 70, 281, 19))
        self.label_version.setObjectName(_fromUtf8("label_version"))
        self.label_qt_python = QtGui.QLabel(DialogAbout)
        self.label_qt_python.setGeometry(QtCore.QRect(160, 270, 261, 19))
        self.label_qt_python.setObjectName(_fromUtf8("label_qt_python"))

        self.retranslateUi(DialogAbout)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(_translate("DialogAbout", "Dialog", None))
        self.label_2.setText(_translate("DialogAbout", "PerlustroC 2018", None))
        self.label_3.setText(_translate("DialogAbout", "Developer: Huesca Morales Francisco Rafael", None))
        self.label_4.setText(_translate("DialogAbout", "Created with:", None))
        self.label_5.setText(_translate("DialogAbout", "Email: pacohm94@gmail.com", None))
        self.label_version.setText(_translate("DialogAbout", "Version:", None))
        self.label_qt_python.setText(_translate("DialogAbout", "TextLabel", None))

import perlustroC_resources_rc
