# calibration_torsi.py
from PySide6.QtSql import QSqlQuery

class CalibrationTorsi:
    def __init__(self, sql_db):
        self.db = sql_db
        if not self.db.isOpen():
            print("[CalibrationTorsi] DB tidak terbuka")
            return
    def get_factor(self):
        query = QSqlQuery("SELECT torque_cal_factor FROM sensor_data ORDER BY id DESC LIMIT 1", self.db)
        if query.next():
            return float(query.value(0))
        return 1.000

    def set_factor(self, value):
        query = QSqlQuery(self.db)
        query.prepare("INSERT INTO sensor_data (torque_cal_factor) VALUES (:factor)")
        query.bindValue(":factor", value)
        if not query.exec():
            print("[CalibrationTorsi] Gagal Menyimpan Faktor Kalibrasi:", query.lastError().text())