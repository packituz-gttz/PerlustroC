# coding=utf-8
import re
import sys
from collections import deque
import array
import pyqtgraph as pg
import serial
import serial.tools.list_ports
from PyQt4.Qt import QSettings, QVariant, QThread, QMutex, QTimer
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import QApplication, QMainWindow, QLabel, QComboBox

import AboutDialog
import Settings
import Temperature
import convertFahrenheit
import time

APP_VERSION = '1.0.0'
APP_NAME = 'PerlustroC'
ORG_NAME = 'Gatituz Inc'
ORG_DOMAIN = 'www.gatituz.duckdns.org'

mutex = QMutex()


class MainWindow(Temperature.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(APP_NAME)

        self.array_values = array.array('h')

        self.list_x = [x for x in xrange(0, 60)]

        self.load_save_settings()

        self.label_usb = QLabel('USB Port:')
        self.celsius = unicode(u'°C')

        self.dialog_settings = Settings.Settings(self.apply_settings,
                                                 self, self.settings)
        self.dialog_about = AboutDialog.AboutDialog(self, APP_VERSION)

        self.timer_updater = QTimer(self)

        self.combobox_usb = QComboBox(self)
        self.toolBar.addWidget(self.label_usb)
        self.toolBar.addWidget(self.combobox_usb)

        self.update_devices_list()
        self.create_plot()

        self.button_start.clicked.connect(self.start_thread)
        self.actionReload.triggered.connect(self.update_devices_list)

        self.timer_updater.timeout.connect(self.update_plot)
        self.actionSettings.triggered.connect(self.show_settings)
        self.actionInfo.triggered.connect(self.show_about)

    def load_save_settings(self):
        self.settings = {'width': 2,
                         'color': 'blue',
                         'x_grid': True,
                         'y_grid': True,
                         'grid_opacity': 0.5}
        settings = QSettings()

        self.settings['width'] = settings.value('width',
                                                self.settings.get('width')).toInt()[0]
        self.settings['color'] = settings.value('color',
                                                self.settings.get('color')).toString()
        self.settings['x_grid'] = settings.value('x_grid',
                                                 self.settings.get('x_grid')).toBool()
        self.settings['y_grid'] = settings.value('y_grid',
                                                 self.settings.get('y_grid')).toBool()
        self.settings['grid_opacity'] = settings.value('grid_opacity',
                                                       self.settings.get('grid_opacity')).toFloat()[0]

    def show_settings(self):
        if not self.dialog_settings.isVisible():
            self.dialog_settings.show()
            self.dialog_settings.raise_()
            self.dialog_settings.activateWindow()

    def show_about(self):
        if not self.dialog_about.isVisible():
            self.dialog_about.show()
            self.dialog_about.raise_()
            self.dialog_about.activateWindow()

    def apply_settings(self):
        self.pen = pg.mkPen(width=self.settings.get('width'),
                            color='y')
        self.plotzone.plotItem.showGrid(self.settings.get('x_grid'),
                                        self.settings.get('y_grid'),
                                        self.settings.get('grid_opacity'))

        format_color = 'color: {0}; font: 36pt "Noto Sans";'.format(self.settings.get('color'))
        self.label_temp.setStyleSheet('QLabel {{{0}}} '.format(format_color))

    def create_plot(self):
        self.pen = pg.mkPen(width=self.settings.get('width'), color='y')
        self.plotzone.plotItem.showGrid(self.settings.get('x_grid'),
                                        self.settings.get('y_grid'),
                                        self.settings.get('grid_opacity'))
        self.plotzone.setXRange(0, 59)
        self.plotzone.setYRange(-100, 100)

        format_color = 'color: {0}; font: 36pt "Noto Sans";'.format(self.settings.get('color'))
        self.label_temp.setStyleSheet('QLabel {{{0}}}'.format(format_color))

    def start_thread(self):
        if str(self.button_start.text()) == '&Start':
            print('START')
            del self.array_values[:]
            self.thread_arduino = ThreadArduino(self,
                                                self.combobox_usb.currentText(),
                                                int(float(self.pinbox_alert.text())),
                                                self.checkbox_sound.isChecked())
            self.thread_arduino.finished.connect(self.thread_stopped)
            self.thread_arduino.update_new_value.connect(self.update_temp_val)
            print(id(self.thread_arduino))
            self.thread_arduino.start()
            self.timer_updater.start(2000)
            self.button_start.setText('&Stop')

        else:
            self.button_start.setEnabled(False)
            mutex.lock()
            self.thread_arduino.keep_running = False
            mutex.unlock()
            # TODO This wont go
            start = time.time()
            convertFahrenheit.conv_all(self.array_values)
            print(time.time() - start)

    def thread_stopped(self):
        self.button_start.setEnabled(True)
        self.timer_updater.stop()
        self.button_start.setText('&Start')
        mutex.lock()
        self.thread_arduino.keep_running = True
        mutex.unlock()
        self.thread_arduino.dq_60.clear()

    def update_devices_list(self):
        device_list = serial.tools.list_ports.comports()
        current_arduino = self.combobox_usb.currentText()
        self.combobox_usb.clear()
        for device_index, device in enumerate(sorted(device_list)):
            self.combobox_usb.addItem(device.device)
            if device.device == current_arduino:
                self.combobox_usb.setCurrentIndex(device_index)

    def update_temp_val(self, new_val):
        self.label_temp.setText(' '.join([str(new_val), self.celsius]))
        self.array_values.extend([new_val])

        convertFahrenheit.convert_fahrenheit(new_val)
        print(len(self.array_values))

    def update_plot(self):
        self.plotzone.plot(self.list_x[:len(self.thread_arduino.dq_60)],
                           list(self.thread_arduino.dq_60), clear=True,
                           pen=self.pen)

    def closeEvent(self, QCloseEvent):
        settings = QSettings()
        settings.setValue('width', QVariant(self.settings['width']))
        settings.setValue('color', QVariant(self.settings['color']))
        settings.setValue('x_grid', QVariant(self.settings['x_grid']))
        settings.setValue('y_grid', QVariant(self.settings['y_grid']))
        settings.setValue('grid_opacity',
                          QVariant(self.settings['grid_opacity']))


class ThreadArduino(QThread):
    update_new_value = Signal(int)

    def __init__(self, parent=None, device=None, temp_alert=None,
                 sound_alert=False):
        super(ThreadArduino, self).__init__(parent)
        self.keep_running = True
        self.dq_60 = deque(maxlen=60)
        self.serial_connection = None
        self.device = str(device)
        self.baud = 9600
        self.temp_alert = temp_alert
        self.sound_alert = sound_alert

        self.sound_test = SoundEnabled()

    def run(self):
        mutex.lock()
        try:
            self.serial_connection = serial.Serial(self.device, 9600,
                                                   timeout=4)
            while self.keep_running:
                mutex.unlock()
                try:
                    temp_val = self.serial_connection.readline()
                    res_re = re.search(';[0-9]+.[0-9]+;', temp_val)
                    if res_re is not None:
                        val_int = int(float(temp_val.split(';')[1]))
                        self.dq_60.appendleft(val_int)
                        self.update_new_value.emit(val_int)
                        self.sound_test.check(self.sound_alert,
                                              self.temp_alert, val_int)
                        # if self.sound_alert:
                        #     if val_int > self.temp_alert:
                        #         print('\a')
                except IndexError:
                    print("Err int")
                self.sleep(2)

        except (serial.SerialException, AttributeError):
            print("ERR CON")
        print("DONE")
        mutex.unlock()


class SoundEnabled:
    def __init__(self):
        pass

    def check(self, sound_alert, temp_alert, val_int):
        if sound_alert:
            self.check = self.check_post_enabled
        else:
            self.check = self.check_post_disabled

    def check_post_enabled(self, sound_alert, temp_alert, val_int):
        if val_int > temp_alert:
            print('\a')

    def check_post_disabled(self, sound_alert, temp_alert, val_int):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName(ORG_NAME)
    app.setOrganizationDomain(ORG_DOMAIN)

    window = MainWindow()
    window.show()
    app.exec_()
