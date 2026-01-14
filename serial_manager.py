# serial_manager.py
import serial
import threading
class SerialManager():
    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.running = False
        self.data_callback = None
        self.thread = None #simpan thread untuk membaca data serial
    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            self.running = True
            self.thread = threading.Thread(target=self.run, daemon=True) #buat thread baru
            self.thread.start()
            self.pause = False   #INI BEDA
            print(f"[CONNECTED] {self.port} @ {self.baudrate} baud")
            return True
        except Exception as e:
            print("[ERROR CONNECTING]", e)
            return False
    def run(self):
        while self.running:
            try:
                if self.pause: #INI BEDA
                    continue #lewati baca kalau sedang di pause INIBEDA
                if self.ser and self.ser.in_waiting:
                    line = self.ser.readline().decode('utf-8').strip()
                    if line and self.data_callback:
                        self.data_callback(line)
            except Exception as e:
                print("[ERROR READING]", e)
    def pause(self):
        print("[SERIAL] Paused")
        self.paused = True
    def resume(self):
        print("[SERIAL] Resumed")
        self.paused = False
    def stop(self):
        self.running = False
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("[DISCONNECTED]")
        self.thread = None # reset thread agar bisa dibuat ulang saat koneksi baru
