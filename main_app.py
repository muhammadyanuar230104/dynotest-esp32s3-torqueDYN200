# main_app.py 
import os
import sys
import csv
import math
import pyqtgraph as pg
import pandas as pd
import serial.tools.list_ports
from datetime import datetime
from PySide6.QtWidgets import (QApplication,QMainWindow,QGridLayout,QVBoxLayout,QMessageBox,QTableView,QInputDialog, QCheckBox, QSizePolicy)
from PySide6.QtCore import Qt, QTimer, Slot, Signal, QSize
from threading import Lock
from main_ui import Ui_MainWindow
from serial_manager import SerialManager
from database import DatabaseManager
from calibration.calibration_torsi import CalibrationTorsi
from calibration.calibration_rpm import CalibrationRPM
from export.export_widget_1 import (export_to_csv_1, export_to_xlsx_1, export_to_pdf_1, export_to_png_1)
from export.export_database import (export_to_pdf_2, export_to_xlsx_2, export_to_csv_2)
from export.export_database_preview import (export_to_pdf_3)
from export.export_widget_3 import (export_to_png_3)
from export.export_widget_5 import (export_to_png_5)
from export.export_widget_4 import (export_to_png_4)
from export.export_widget_6 import (export_to_png_6)
from export.export_widget_9 import (export_to_png_9)
from speedometer.widget_speedometer import SpeedometerWidget
from speedometer.widget_power import PowerWidget
from speedometer.widget_torsi import TorqueGaugeWidget
from grafik.widget_1 import Widget1
from grafik.widget_9_preview import Widget9TorqueOnly
from grafik.widget_5_file import Widget5
from grafik.widget_6_preview import Widget6PowerOnly
from grafik.widget_4_preview import Widget4HPOnly
class MainApp(QMainWindow):
    serial_data_received = Signal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Dynotest")
        #disimpan data terakhir
        self.data_lock = Lock()
        self.last_data = {'rpm' : None, 'rpm_cal': None, 'rpm_cal_factor': None, 'torque' : None, 'torque_cal': None, 'torque_cal_factor': None, 'power' : None}
        #tetapkan halaman awal ke dashboard page
        self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page)      
        # Koneksi tombol connect/disconnect
        self.serial_data_received.connect(self.handle_serial_data)
        self.ui.button_connect.clicked.connect(self.connect_serial)
        self.ui.button_disconnect.clicked.connect(self.disconnect_serial)
        #tombol resume dan stop 
        self.ui.button_stop.clicked.connect(self.pause_data)
        self.ui.button_resume.clicked.connect(self.resume_data)
        # flag baru
        self.data_paused = False #kontrol grafik dan database
        self.is_connected = False #status koneksi serial 
        # Inisialisasi database
        self.db = DatabaseManager()  
        #tombol reset database
        self.ui.button_reset_database.clicked.connect(self.reset_database)
        #tambahkan Qaction untuk menampilkan halaman dashboard
        self.ui.actionopen_dashboard.triggered.connect(self.show_dashboard_page)
        self.ui.actionopen_file.triggered.connect(self.show_file_page)
        self.ui.actionopen_preview.triggered.connect(self.show_preview_page)
        self.ui.actionopen_about.triggered.connect(self.show_about_dialog)
        #Default kalibrasi adalah tidak aktif
        self.ui.check_box_calibration.setChecked(False)
        self.ui.check_box_cut_off.setChecked(True)
        #konfigurasi calibration torque
        self.calibration = CalibrationTorsi(self.db.sql_db)
        self._torque_calibration_factor = self.calibration.get_factor()
        self.ui.label_cal_torque.setText(f"Torsi: {self._torque_calibration_factor:.3f}")
        self.ui.actionopen_calibration_torsi.triggered.connect(self.set_torque_calibration)
        #konfigurasi calibration rpm
        self.calibration_rpm = CalibrationRPM(self.db.sql_db)
        self._rpm_calibration_factor = self.calibration_rpm.get_factor()
        self.ui.label_cal_rpm.setText(f"RPM: {self._rpm_calibration_factor:.3f}")
        self.ui.actionopen_calibration_rpm.triggered.connect(self.set_rpm_calibration)
        #connect combo box and button untuk print data
        self.ui.print_dynotest.activated.connect(self.handle_print_dynotest)
        self.ui.print_database.activated.connect(self.handle_print_database)
        self.ui.button_pdf_preview.clicked.connect(self.handle_print_preview) #tombol untuk ke halaman preview          
        self.ui.button_kw.clicked.connect(self.handle_print_kw) #tombol untuk ke halaman grafik kw
        self.ui.button_hp.clicked.connect(self.handle_print_hp) #tombol untuk ke halaman grafik hp
        self.ui.button_hp_preview.clicked.connect(self.handle_hp_preview) #tombol untuk ke halaman grafik hp preview
        self.ui.button_power_preview.clicked.connect(self.handle_kw_preview) #tombol untuk ke halaman grafik kw preview
        self.ui.button_torsi_preview.clicked.connect(self.handle_torsi_preview) #tombol untuk ke halaman grafik torsi preview
        # Inisialisasi halaman grafik
        self.plot_widget_1 = self.add_widget_to_layout(self.ui.widget_1, Widget1)
        self.plot_widget_3 = self.add_widget_to_layout(self.ui.widget_3, Widget1)
        self.plot_widget_5 = self.add_widget_to_layout(self.ui.widget_5, Widget5)
        #halaman preview
        self.plot_widget_4 = self.add_widget_to_layout(self.ui.widget_4, Widget4HPOnly)
        self.plot_widget_6 = self.add_widget_to_layout(self.ui.widget_6, Widget6PowerOnly)
        self.plot_widget_9 = self.add_widget_to_layout(self.ui.widget_9, Widget9TorqueOnly)
        #widget untuk speedometer
        self.torque = self.add_widget_to_layout(self.ui.widget_8, TorqueGaugeWidget)
        self.speedo = self.add_widget_to_layout(self.ui.widget_2, SpeedometerWidget)
        self.power = self.add_widget_to_layout(self.ui.widget_7, PowerWidget)
        # Konfigurasikan tableView
        self.db.configure_table_view(self.ui.tableView)
        # Timer untuk auto refresh table setiap 3 detik
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_table)
        self.refresh_timer.start(100)  # 3000 ms = 3 detik
        #set pilih warna speedometer
        self.ui.pilih_warna.currentIndexChanged.connect(self.apply_theme_to_speedometer)
        self.ui.pilih_speedometer.currentIndexChanged.connect(self.apply_theme_to_speedometer)   
        # inisialisasi awal
        self.update_available_ports()  
        #refresh port tiap detik
        self.port_timer = QTimer(self)
        self.port_timer.timeout.connect(self.update_available_ports)
        self.port_timer.start(1000)  # 1000ms = 1 detik
        #fungsi auto cut off
        self.peak_rpm = 0 #menyimpan nilai rpm tertinggi
        self.auto_cutoff_triggered = False #menandakan apakah auto cut off sudah aktif
        #fungsi tracking auto cut off widget speedometer
        self.max_rpm_cal = 0
        self.max_torque_cal = 0
        self.max_power = 0
    @Slot(str)
    def handle_serial_data(self, line):
        with self.data_lock:
            if self.data_paused:
                return # data masuk diabaikan saat mode paused
        try:
            parts = line.strip().split('|')
            if len(parts) != 3:
                raise ValueError("Data tidak lengkap")
            # Ambil dan convert dengan aman
            rpm = int (parts[0].split(':')[1].strip())
            torque = float (parts[1].split(':')[1].strip())
            power = int (parts[2].split(':')[1].strip())
            # perlu faktor kalibrasinya saja
            torque_cal_factor = self.get_torque_calibration_factor()
            torque_cal = torque * torque_cal_factor
            #faktor kalibrasi rpm
            rpm_cal_factor = self.get_rpm_calibration_factor()
            rpm_cal = rpm * rpm_cal_factor
            # Perhitungan Power (Optimasi logika)
            if torque >= 0:  # Tangani nilai torsi positif
                power_cal = (torque_cal * rpm_cal * 2 * 3.1415) / 60
            else:  # Tangani nilai torsi negatif
                power_cal = abs((torque_cal * rpm_cal * 2 * 3.1415) / 60)
            power_to_use = int(power_cal if rpm_cal_factor != 1 or torque_cal_factor != 1 else power)
            #tampilkan di gauge
            self.power.setValue(power_to_use)
            self.speedo.setValue(rpm_cal) #update speedometer
            self.torque.setValue(torque_cal) 
            # Simpan & tampilkan di grafik MASIH BELUM SELESAI SEMUA YANG MASUK
            self.db.insert_data(rpm, rpm_cal, rpm_cal_factor, torque, torque_cal, torque_cal_factor, power_to_use)
            self.plot_widget_1.append_data(rpm_cal, torque_cal, power_to_use)
            self.plot_widget_3.append_data(rpm_cal, torque_cal, power_to_use)            
            self.plot_widget_5.append_data(rpm_cal, torque_cal, power_to_use)
            #page preview
            self.plot_widget_4.append_data(rpm_cal, power_to_use)
            self.plot_widget_6.append_data(rpm_cal, power_to_use)
            self.plot_widget_9.append_data(rpm_cal, torque_cal)
            #auto cut off logic
            if not self.data_paused and self.ui.check_box_cut_off.isChecked(): #periksa auto cut off aktif?
                if rpm_cal > self.peak_rpm:
                    self.peak_rpm = rpm_cal #simpan nilai puncak baru
                    self.auto_cutoff_triggered = False #reset jika naik lagi
                elif rpm_cal <= self.peak_rpm - 10 and not self.auto_cutoff_triggered:
                    self.auto_cutoff_triggered = True
                    self.pause_data() #panggil pause data
            # track nilai maksimum untuk semua gauge
            if rpm_cal > 0: 
                self.max_rpm_cal = max(self.max_rpm_cal, rpm_cal)
            if torque_cal > 0:
                self.max_torque_cal = max(self.max_torque_cal, torque_cal)
            if power > 0:
                self.max_power = max(self.max_power, power)
        except Exception as e:
            print("Parsing error:", e)
    def add_widget_to_layout(self, container_widget, custom_widget_class):
        widget = custom_widget_class()
        layout = QVBoxLayout(container_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widget)
        return widget
    def update_available_ports(self):
        from serial.tools import list_ports
        current_ports = [port.device for port in serial.tools.list_ports.comports()]
        existing_ports = [self.ui.box_port.itemText(i) for i in range(self.ui.box_port.count())]
        if current_ports != [e for e in existing_ports if e != "Pilih Port"]:
            self.ui.box_port.clear()
            self.ui.box_port.addItem("Pilih Port")
            self.ui.box_port.addItems(current_ports)
            self.ui.box_port.setCurrentIndex(0)
    def connect_serial(self):
        if self.is_connected:
            QMessageBox.warning(self, "Koneksi Gagal", "Sudah terhubung! Silahkan klik disconnect terlebih dahulu")
            return
        selected_port = self.ui.box_port.currentText()
        selected_baud = "38400"
        if not selected_port or selected_port == "Pilih Port":
            QMessageBox.warning(self, "Koneksi Gagal", "Silakan pilih PORT terlebih dahulu.")
            return
        try:
            #setup koneksi serial
            self.refresh_timer.stop()   #1. stop auto refresh agar tidak bentrok saat reset
            self.db.reset_table()       #2. reset tabel
            self.refresh_table()        #3. refresh tampilan secara manual
            self.refresh_timer.start(100)  #4. start ulang timer 
            baudrate = int(selected_baud)  #5. mulai koneksi serial
            self.reader = SerialManager(selected_port, baudrate)
            self.reader.data_callback = self.serial_data_received.emit
            if self.reader.connect():
                self.ui.label_port.setText(f"Port : {selected_port}")
                self.ui.label_baudrate.setText(f"Baudrate : {baudrate}")
                self.is_connected = True #menandakan sudah koneksi 
                self.data_paused = False #data siap untuk dibaca
                self.reset_all_graphs() #reset grafik saat connect
                # Membuat QMessageBox
                msg_box = QMessageBox(self)
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Koneksi Berhasil")
                msg_box.setText("Serial Terhubung dan Database di Reset")
                # Tampilkan QMessageBox
                msg_box.show()
                # Timer untuk menutup QMessageBox setelah 300 ms
                QTimer.singleShot(1500, msg_box.close)
            else:
                QMessageBox.critical(self, "Gagal", f"Tidak bisa connect ke {selected_port} @ {baudrate}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saat koneksi: {e}")
    def disconnect_serial(self):
        if hasattr(self, 'reader') and self.reader:
            self.reader.stop() #menghentikan pembacaan data serial
            self.is_connected = False #status koneksi menjadi false
            self.data_paused = False #pastikan data pause juga
            self.ui.label_port.setText("Port : --")
            self.ui.label_baudrate.setText("Baudrate : --")
            QMessageBox.information(self, "Terputus", "koneksi serial dihentikan")
    def pause_data(self):
        if self.is_connected:
            self.data_paused = True
            self.reader.stop() #stop pembacaan data serial
            #untuk membuat garis ke nilai peak rpm
            self.speedo.setValue(self.max_rpm_cal)
            self.torque.setValue(self.max_torque_cal)
            self.power.setValue(self.max_power)
            # Membuat QMessageBox
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Berhenti")
            msg_box.setText("Pembacaan data dihentikan")
            # Tampilkan QMessageBox
            msg_box.show()
            # Timer untuk menutup QMessageBox setelah 300 ms
            QTimer.singleShot(1500, msg_box.close)
            #QMessageBox.information(self, "Berhenti", "Pembacaan data dihentikan")
    def resume_data(self):
        if self.is_connected and self.data_paused:
            try: 
                #reset grafik tapi tidak dengan database nya
                self.reset_all_graphs()
                #buat ulang koneksi serial
                self.reader = SerialManager(self.reader.port, self.reader.baudrate)
                self.reader.data_callback = self.serial_data_received.emit
                if self.reader.connect():
                    self.data_paused = False #data siap untuk dibaca
                    self.peak_rpm = 0 #reset peak rpm
                    self.max_rpm_cal = 0
                    self.max_torque_cal = 0
                    self.max_power = 0
                    self.auto_cutoff_triggered = False #reset flag cut off
                    #QMessageBox.information(self, "Lanjutkan", "Pembacaan data dilanjutkan")
                else:
                    QMessageBox.critical(self, f"Tidak bisa connect ke {self.reader.port} @ {self.reader.baudrate}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error saat koneksi: {e}")                         
    def closeEvent(self, event):
        if hasattr(self, 'reader') and self.reader:
            self.reader.stop()
        self.db.close()
        event.accept()
    def reset_database(self):
        self.reader.pause
        self.db.reset_table()
        # Membuat QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Reset Berhasil")
        msg_box.setText("Database Berhasil Direset")
        # Tampilkan QMessageBox
        msg_box.show()
        # Timer untuk menutup QMessageBox setelah 300 ms
        QTimer.singleShot(1500, msg_box.close)
    def reset_all_graphs(self):
        self.plot_widget_1.reset_data()
        self.plot_widget_3.reset_data()
        self.plot_widget_4.reset_data()
        self.plot_widget_5.reset_data()
        self.plot_widget_6.reset_data()
        self.plot_widget_9.reset_data()
    def refresh_table(self):
        self.db.model.select()
        self.ui.tableView.resizeColumnsToContents()
    def get_rpm_calibration_factor(self):
        return self._rpm_calibration_factor
    def set_rpm_calibration(self):
        if not self.ui.check_box_calibration.isChecked():
            QMessageBox.warning(self, "Akses Ditolak", "Aktifkan Enable Cal Untuk Menyimpan Kalibrasi.")
            return
        try:
            value, ok = QInputDialog.getDouble(
                self,
                "Set Kalibrasi RPM",
                "Masukkan faktor kalibrasi RPM:",
                decimals=3,
                minValue=0.0,
                maxValue=100.0,
                value=self.get_rpm_calibration_factor())
            if ok:
                self._rpm_calibration_factor = value
                self.calibration_rpm.set_factor(value)
                QMessageBox.information(self, "Sukses", f"Faktor kalibrasi diubah ke {value:.3f}")
                self.ui.label_cal_rpm.setText(f"{self._rpm_calibration_factor:.3f}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal set kalibrasi: {e}")
    def get_torque_calibration_factor(self):
        return self._torque_calibration_factor
    def set_torque_calibration(self):
        if not self.ui.check_box_calibration.isChecked():
            QMessageBox.warning(self, "Akses Ditolak", "Aktifkan Enable Cal Untuk Menyimpan Kalibrasi.")
            return
        try:
            value, ok = QInputDialog.getDouble(
                self,
                "Set Kalibrasi Torque",
                "Masukkan faktor kalibrasi torque:",
                decimals=3,
                minValue=0.0,
                maxValue=100.0,
                value=self.get_torque_calibration_factor())
            if ok:
                self._torque_calibration_factor = value
                self.calibration.set_factor(value)
                QMessageBox.information(self, "Sukses", f"Faktor kalibrasi diubah ke {value:.3f}")
                self.ui.label_cal_torque.setText(f"{self._torque_calibration_factor:.3f}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal set kalibrasi: {e}")
    def handle_print_dynotest(self, index):
        if index == 0:
            return #skip ke pilih format gambar
        elif index == 1:
            export_to_xlsx_1(self.db, self)
        elif index == 2:
            export_to_csv_1(self.db, self)
        elif index == 3:
            export_to_png_1(self.plot_widget_1, self)
        elif index == 4:
            export_to_pdf_1(self.db, self)
        #reset combo box ke default
        QTimer.singleShot(100, lambda: self.ui.print_dynotest.setCurrentIndex(0))
    def handle_print_database(self, index):
        if index == 0:
            return
        elif index == 1:
            export_to_pdf_2(self.db, self)
        elif index == 2:
            export_to_xlsx_2(self.db, self)
        elif index == 3:
            export_to_csv_2(self.db, self)
        QTimer.singleShot(100, lambda: self.ui.print_database.setCurrentIndex(0))
    def handle_print_preview(self):
        try:
            export_to_pdf_3(self.db, self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan PDF preview: {e}")
    def handle_print_kw(self):
        try:
            export_to_png_3(self.plot_widget_3, self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan KW gambar: {e}")
    def handle_print_hp(self):
        try:
            export_to_png_5(self.plot_widget_5, self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan HP gambar: {e}")
    def handle_hp_preview(self):
        try: 
            export_to_png_4(self.plot_widget_4, self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan HP preview: {e}")
    def handle_kw_preview(self):
        try:
            export_to_png_6(self.plot_widget_6, self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan Power preview: {e}")
    def handle_torsi_preview(self):
        try:
            export_to_png_9(self.plot_widget_9, self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan Torque preview: {e}")
    def show_dashboard_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page)
    def show_file_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.file_page)
    def show_preview_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.preview_page)
    def show_about_dialog(self):
        # Buat dialog "About"
        about_message = QMessageBox(self)
        about_message.setIcon(QMessageBox.Information)
        about_message.setWindowTitle("Tentang Aplikasi")
        about_message.setText(
            "<h2>Dynotest</h2>"
            "<p>Aplikasi ini dirancang untuk memonitor dan menganalisis data dinamometer secara real-time.</p>"
            "<hr>"
            "<p><strong>Versi:</strong> 1.0</p>"
            "<p><strong>Dibuat oleh:</strong> Muhammad Yanuar</p>"
            "<p><strong>Dibangun dengan:</strong> Python dan PySide6</p>"
            "<p><strong>Disetujui oleh:</strong> Dr. Muhammad Nur Yuniarto, ST, IPM, AEng</p>"
            "<hr>"
            "<h3>Kontak</h3>"
            "<p><strong>Email:</strong> muhammadyanuar2314@gmail.com</p>"
            "<p><strong>LinkedIn:</strong> <a href='https://www.linkedin.com/in/muhammadyanuar' target='_blank'>linkedin.com/in/muhammadyanuar</a></p>"
            "<hr>"
            "<p>Hak Cipta &copy; 2025 Muhammad Yanuar. Semua hak cipta dilindungi.</p>"
        )
        about_message.setStandardButtons(QMessageBox.Ok)
        about_message.exec()
    def apply_theme_to_speedometer(self):
        theme_name = self.ui.pilih_warna.currentText()
        target = self.ui.pilih_speedometer.currentText()
        if target.lower() == "rpm":
            self.speedo.setTheme(theme_name)
        elif target.lower() == "power (w)":
            self.power.setTheme(theme_name)
        elif target.lower() == "torsi (nm)":
            self.torque.setTheme(theme_name)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
