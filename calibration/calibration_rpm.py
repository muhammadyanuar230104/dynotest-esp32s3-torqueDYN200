# calibration_rpm.py
from PySide6.QtSql import QSqlQuery

class CalibrationRPM:
    def __init__(self, sql_db):
        self.db = sql_db
        if not self.db.isOpen():
            print("[CalibrationRPM] DB tidak terbuka")
            return
    def get_factor(self):
        query = QSqlQuery("SELECT factor FROM rpm_settings LIMIT 1", self.db)
        if query.next():
            return float(query.value(0))
        return 1.000 #jika belum ada data (default)
    def set_factor(self, value):
        query = QSqlQuery(self.db)
        query.prepare("INSERT INTO sensor_data (rpm_cal_factor) VALUES (:factor)")
        query.bindValue(":factor", value)
        if not query.exec():
            print("[CalibrationRPM] Gagal Menyimpan Faktor Kalibrasi:", query.lastError().text())
            
            