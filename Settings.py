import DialogSettings
from PyQt4.QtGui import QDialog, QDialogButtonBox

class Settings(DialogSettings.Ui_Dialog, QDialog):
    def __init__(self, callback, parent=None, settings=None):
        super(Settings, self).__init__(parent)
        self.setupUi(self)

        self.callback = callback
        self.settings = settings

        self.set_settings()
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).setDefault(False)
        self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)
        self.buttonBox.button(QDialogButtonBox.Cancel).setAutoDefault(True)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.reset_to_defaults)

        self.combobox_text_color.currentIndexChanged.connect(self.apply_changes)
        self.doubles_spinbox_line_width.valueChanged.connect(self.apply_changes)
        self.double_spinbox_opacity.valueChanged.connect(self.apply_changes)
        self.checkbox_x.clicked.connect(self.apply_changes)
        self.checkbox_y.clicked.connect(self.apply_changes)

    def set_settings(self):
        self.combobox_text_color.setCurrentIndex(self.combobox_text_color.findText(self.settings.get('color')))
        self.checkbox_x.setChecked(self.settings.get('x_grid'))
        self.checkbox_y.setChecked(self.settings.get('y_grid'))
        self.double_spinbox_opacity.setValue(self.settings.get('grid_opacity'))
        self.doubles_spinbox_line_width.setValue(self.settings.get('width'))

    def apply_changes(self):
        self.settings['color'] = self.combobox_text_color.currentText()
        self.settings['x_grid'] = self.checkbox_x.isChecked()
        self.settings['y_grid'] = self.checkbox_y.isChecked()
        self.settings['grid_opacity'] = self.double_spinbox_opacity.value()
        self.settings['width'] = self.doubles_spinbox_line_width.value()

        self.callback()

    def reset_to_defaults(self):
        settings_defaults = {'width': 2, 'color': 'blue', 'x_grid': True, 'y_grid': True, 'grid_opacity': 0.5}

        self.combobox_text_color.setCurrentIndex(self.combobox_text_color.findText(settings_defaults.get('color')))
        self.checkbox_x.setChecked(settings_defaults.get('x_grid'))
        self.checkbox_y.setChecked(settings_defaults.get('y_grid'))
        self.double_spinbox_opacity.setValue(settings_defaults.get('grid_opacity'))
        self.doubles_spinbox_line_width.setValue(settings_defaults.get('width'))