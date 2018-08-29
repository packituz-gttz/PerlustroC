# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSettings.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 272)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.combobox_text_color = QtGui.QComboBox(self.groupBox_2)
        self.combobox_text_color.setObjectName(_fromUtf8("combobox_text_color"))
        self.combobox_text_color.addItem(_fromUtf8(""))
        self.combobox_text_color.addItem(_fromUtf8(""))
        self.combobox_text_color.addItem(_fromUtf8(""))
        self.combobox_text_color.addItem(_fromUtf8(""))
        self.combobox_text_color.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.combobox_text_color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.doubles_spinbox_line_width = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubles_spinbox_line_width.setMaximum(10.0)
        self.doubles_spinbox_line_width.setProperty("value", 2.0)
        self.doubles_spinbox_line_width.setObjectName(_fromUtf8("doubles_spinbox_line_width"))
        self.horizontalLayout_2.addWidget(self.doubles_spinbox_line_width)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.double_spinbox_opacity = QtGui.QDoubleSpinBox(self.groupBox)
        self.double_spinbox_opacity.setMaximum(1.0)
        self.double_spinbox_opacity.setSingleStep(0.1)
        self.double_spinbox_opacity.setProperty("value", 0.5)
        self.double_spinbox_opacity.setObjectName(_fromUtf8("double_spinbox_opacity"))
        self.horizontalLayout_4.addWidget(self.double_spinbox_opacity)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkbox_y = QtGui.QCheckBox(self.groupBox)
        self.checkbox_y.setObjectName(_fromUtf8("checkbox_y"))
        self.horizontalLayout.addWidget(self.checkbox_y)
        self.checkbox_x = QtGui.QCheckBox(self.groupBox)
        self.checkbox_x.setObjectName(_fromUtf8("checkbox_x"))
        self.horizontalLayout.addWidget(self.checkbox_x)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.buttonBox.raise_()
        self.combobox_text_color.raise_()
        self.label.raise_()
        self.doubles_spinbox_line_width.raise_()
        self.groupBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.double_spinbox_opacity.raise_()
        self.double_spinbox_opacity.raise_()
        self.groupBox_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_2.setTitle(_translate("Dialog", "General", None))
        self.label.setText(_translate("Dialog", "Text Color:", None))
        self.combobox_text_color.setItemText(0, _translate("Dialog", "blue", None))
        self.combobox_text_color.setItemText(1, _translate("Dialog", "orange", None))
        self.combobox_text_color.setItemText(2, _translate("Dialog", "red", None))
        self.combobox_text_color.setItemText(3, _translate("Dialog", "white", None))
        self.combobox_text_color.setItemText(4, _translate("Dialog", "yellow", None))
        self.groupBox.setTitle(_translate("Dialog", "Grid", None))
        self.label_2.setText(_translate("Dialog", "Line Width:", None))
        self.label_3.setText(_translate("Dialog", "Opacity:", None))
        self.checkbox_y.setText(_translate("Dialog", "Y Axis", None))
        self.checkbox_x.setText(_translate("Dialog", "X Axis", None))

