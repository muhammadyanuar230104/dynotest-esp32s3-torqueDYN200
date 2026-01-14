
#define RXD2 18  // RX ESP32 ke RX RS485
#define TXD2 17  // TX ESP32 ke TX RS485
void setup() {
  Serial.begin(115200); // Debugging ke Serial Monitor
  Serial2.begin(38400, SERIAL_8N1, RXD2, TXD2); // RS485
}
void loop() {
  bacaSensor(0x00, "Torsi (Nm)");   // Baca data torsi
  bacaSensor(0x02, "Speed (RPM)");  // Baca data kecepatan
  bacaSensor(0x04, "Power (Watt)"); // Baca data daya
  delay(1000);
}
void bacaSensor(byte address, String label) {
  byte request[] = {0x01, 0x03, 0x00, address, 0x00, 0x02, 0x00, 0x00};
  uint16_t crc = hitungCRC(request, 6); // Hitung CRC
  request[6] = crc & 0xFF;
  request[7] = (crc >> 8) & 0xFF;
  Serial2.write(request, sizeof(request));
  Serial.print("Mengambil data ");
  Serial.println(label);
  delay(500);  // Tunggu sensor merespons
  if (Serial2.available()) {
    Serial.print(label);
    Serial.print(": ");
    while (Serial2.available()) {
      Serial.print(Serial2.read(), HEX);
      Serial.print(" ");
    }
    Serial.println();
  } else {
    Serial.println("Tidak ada respons.");
  }
}
// Fungsi CRC16 untuk MODBUS
uint16_t hitungCRC(byte *data, byte length) {
  uint16_t crc = 0xFFFF;
  for (byte i = 0; i < length; i++) {
    crc ^= data[i];
    for (byte j = 0; j < 8; j++) {
      if (crc & 1) {
        crc >>= 1;
        crc ^= 0xA001;
      } else {
        crc >>= 1;
      }
    }
  }
  return crc;
}
