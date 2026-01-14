#include <ModbusMaster.h>

#define RXD2 17  // Sesuaikan dengan RX ESP32-S3
#define TXD2 18 // Sesuaikan dengan TX ESP32-S3

HardwareSerial SerialMod(1);  // Gunakan UART2

ModbusMaster node1;
#define modbusaddr1 1 

//variabel simpan data
unsigned long torque, speed, power;

void preTransmission();
void postTransmission();
unsigned long readULongValue (ModbusMaster& node, uint16_t regAddress);

void setup() {
    Serial.begin(115200);    // Debugging
    SerialMod.begin(9600, SERIAL_8N1, RXD2, TXD2);  // Baud rate 9600, N81
    
    node1.begin(modbusaddr1, SerialMod); // ID device 1
    node1.preTransmission(preTransmission); // 
    node1.postTransmission(postTransmission); // 
    //node1.begin(modbusaddr1, SerialMod); // 
    Serial.println("Modbus monitoring ready");

    delay(500);
}

void loop() {
    
    //baca nilai dari slave pertama
    torque = readULongValue(node1, 0x0000);
    //speed = readULongValue(node1, 2);
    //power = readULongValue(node1, 4);


     Serial.print("Torque (Nm): ");
     Serial.println(torque * 0.0001);  // Decimal point 2
     
     //Serial.print("Speed (RPM): ");
     //Serial.println(speed);

     //Serial.print("Power (W): ");
     //Serial.println(power * 0.0001);  // Data dalam 10W, dikonversi ke W
  
    delay(1000);  // Baca data tiap 1 detik
}


// fungsi untuk membaca nilai unsigned long dari register modbus 
unsigned long readULongValue(ModbusMaster& node, uint16_t regAddress) {
  uint8_t result = node.readHoldingRegisters(0x0000, 2); //membaca 2 register (4 bytes)
  
  if (result == node.ku8MBSuccess) {
    uint32_t value = (node.getResponseBuffer(0) << 16) | node.getResponseBuffer(1);
    return value;
  } else {
    Serial.println("Modbus RTU failed at register");
    Serial.print(regAddress);
    Serial.print(" with error code: ");
    Serial.println(result);
    return 0; //nilai default penanganan error
  }
}

void preTransmission(){
}

void postTransmission(){
}