#include <rf4463.hpp>
#include <SPI.h>
 
RF4463 rf4463;
unsigned char rx_len;
unsigned char rx_buf[20];

void setup() {
  Serial.begin(9600);
  while(true) {
    Serial.println("HELLO WORLD");
    delay(500);
  }

  if(!rf4463.init()) {
    Serial.println("Init fail!");
  } else {
    Serial.println("Init success!");
  } 

  if(!rf4463.checkDevice()) {
    Serial.println("Check device failed");
  }
  rf4463.rxInit();

  uint8_t buf[8];
  if(!rf4463.getProperties(RF4463_PROPERTY_MODEM_RSSI_COMP, 8, buf)) {
    Serial.println("Failed to get the comp property");
  }
}

void loop() 
{
  if(rf4463.waitnIRQ()) {
    rf4463.clrInterrupts();
    rx_len=rf4463.rxPacket(rx_buf);  // read rx data
    Serial.print("Received: ");
    Serial.write(rx_buf, rx_len);    // print out by serial
    Serial.println("");
    rf4463.rxInit();
  }
}