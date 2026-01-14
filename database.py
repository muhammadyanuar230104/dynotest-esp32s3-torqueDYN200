# database.py
import sys 
import os
from datetime import datetime
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView, QAbstractItemView, QAbstractScrollArea 
#database manager class
class DatabaseManager:
    def __init__(self, db_path="dynotest.db"):
        #Gunakan resource_path untuk memastikan lokasi absolut
        db_path = self.resource_path(db_path)
        # Setup database connection for QSqlTableModel
        self.sql_db = QSqlDatabase.addDatabase("QSQLITE")
        self.sql_db.setDatabaseName(db_path)
        if not self.sql_db.open():
            print("Failed to connected {db_path}!")
        else:
            print("Database connected {db_path}!")
        self.create_table()
        # Create the model
        self.model = QSqlTableModel(None, self.sql_db)
        self.model.setTable("sensor_data")
        self.model.select()
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'): #pyinstaller support
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    def create_table(self):
        query = QSqlQuery(self.sql_db)
        query.exec('''
            CREATE TABLE IF NOT EXISTS sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rpm INTEGER,
                rpm_cal REAL,
                rpm_cal_factor REAL,
                torque REAL,
                torque_cal REAL,
                torque_cal_factor REAL,
                power INTEGER,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP    
            )
        ''')
    def reset_table(self):
        if not self.sql_db.isOpen():
            print("Database is not open!")
            self.sql_db.open() #pastikan database terbuka sebelum eksekusi
            return
        #Disconnect the model from the database before dropping the table
        self.model.setTable("")  # Disconnect the model from the table
        self.model.clear()  # Clear the model data
        #hapus semua data (bukan drop table)
        query = QSqlQuery(self.sql_db)
        if not query.exec("DROP TABLE IF EXISTS sensor_data"):
            print("Failed to drop table:", query.lastError().text())
        self.create_table() #INIBEDA
        #reconnect model and select
        self.model.setTable("sensor_data")
        #self.model.setSort(self.model.fieldIndex("timestamp"), Qt.DescendingOrder)  # Sort by ID (descending)
        self.model.select()
    def insert_data(self, rpm, rpm_cal, rpm_cal_factor, torque, torque_cal, torque_cal_factor, power):
        if not self.sql_db.isOpen():
            print("Database is not open!")
            return
        timestamp = datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        query = QSqlQuery(self.sql_db)
        query.prepare("""
            INSERT INTO sensor_data (rpm, rpm_cal, rpm_cal_factor, torque, torque_cal, torque_cal_factor, power, timestamp)
            VALUES (:rpm, :rpm_cal, :rpm_cal_factor, :torque, :torque_cal, :torque_cal_factor, :power, :timestamp)
        """)
        query.bindValue(":rpm", rpm)
        query.bindValue(":rpm_cal", rpm_cal)
        query.bindValue(":rpm_cal_factor", rpm_cal_factor)
        query.bindValue(":torque", torque)
        query.bindValue(":torque_cal", torque_cal)
        query.bindValue(":torque_cal_factor", torque_cal_factor)
        query.bindValue(":power", power)
        query.bindValue(":timestamp", timestamp)
        if not query.exec(): 
            print("Failed to insert data:", query.lastError().text())
        else:
            self.model.select()  # Refresh the model to show new data
    #untuk ekspor data ke file csv, xlsx, pdf
    def fetch_all_data(self):
        results = []
        query = QSqlQuery(self.sql_db)
        if query.exec("SELECT timestamp, rpm, rpm_cal, rpm_cal_factor, torque, torque_cal, torque_cal_factor, power FROM sensor_data"):
            while query.next():
                timestamp = query.value(0)
                rpm = query.value(1)
                rpm_cal = query.value(2)
                rpm_cal_factor = query.value(3)
                torque = query.value(4)
                torque_cal = query.value(5)
                torque_cal_factor = query.value(6)
                power = query.value(7)
                results.append((timestamp, rpm, rpm_cal, rpm_cal_factor, torque, torque_cal, torque_cal_factor, power))
        else:
            print("Failed to fetch data:", query.lastError().text())
        return results
    def get_model(self):
        return self.model
    def configure_table_view(self, table_view):
        # Set the model for the table view
        table_view.setModel(self.model)
        # Resize settings
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # Allow manual resizing
        table_view.horizontalHeader().setStretchLastSection(True)
        table_view.resizeRowsToContents()
        # Scroll settings
        table_view.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        table_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        #header settings
        v_header = table_view.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(30)
        # Adjust table size to fit the layout in Qt Designer
        table_view.setShowGrid(True)
        table_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        table_view.setStyleSheet("""
        QTableView {
            gridline-color: blue;
            border: 1px solid #ccc;
            background-color: #ffffff;
            color: black;
            selection-background-color: blue;
        }
        QHeaderView::section {
            background-color: #f2f2f2;  /* Pastikan warna putih diterapkan */
            color: blue;              /* Pastikan warna teks hitam diterapkan */
            padding: 4px;
            border: 1px solid #ccc;
        }
        QTableCornerButton::section {
            border: 1px solid #ccc;
            background-color: #f2f2f2;
        }
        QTableView::item {
            border: 1px solid #ccc;
            color: black;
        }
        """)
    def close(self):
        if self.sql_db.isOpen():
            self.sql_db.close()
