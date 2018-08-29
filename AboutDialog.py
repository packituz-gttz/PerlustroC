from PyQt4.QtGui import QDialog
from PyQt4.Qt import PYQT_VERSION_STR
import DialogAbout
import sys

class AboutDialog(DialogAbout.Ui_DialogAbout, QDialog):
    def __init__(self, parent=None, version=''):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)

        python_version = sys.version.split()[0]

        self.label_version.setText(' '.join(['Version:', version]))
        self.label_qt_python.setText(' '.join(['PyQt', PYQT_VERSION_STR, ' Python', python_version]))
