// rf4463_slave.pde

// Caution:RF4463 module can only work under 3.3V
// please make sure the supply of you board is under 3.3V
// lora supply will destroy RF4463 module!!

// This code runs in slave mode and  works with rf_4463_master.pde 
// Flow:receive packet from master->print to serial->reply
// data of packet is "swwxABCDEFGHIm"

#include<RF4463.h>
#include<SPI.h>
 
RF4463 rf4463;
unsigned char tx_buf[]={"swwxABCDEFGHIm"};
unsigned char val;
unsigned char flag=1;    //  flag of rx mode
unsigned char rx_len;
unsigned char rx_buf[20];

#define DEBUG_RF4463

void setup() {
  Serial.begin(9600);
  if(!rf4463.init()) {
    Serial.println("Init fail!");
  } else {
    Serial.println("Init success!");
  }


  if(!rf4463.checkDevice()) {
    Serial.println("Check device failed");
  }
  rf4463.rxInit();

  uint8_t buf[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
  if(rf4463.getCommand(7,RF4463_CMD_START_RX,buf)) {
    Serial.println("Got the CMD to setup rx");
  }

  for(uint8_t i =  0; i < sizeof(buf); i = i + 1) {
    Serial.println("Write byte: ");
    Serial.write(i);
    Serial.write(buf[i]);
  }

}
void loop() 
{
  if(rf4463.waitnIRQ()) {
    rf4463.clrInterrupts();
    rx_len=rf4463.rxPacket(rx_buf);  // read rx data
    Serial.write(rx_buf, rx_len);    // print out by serial
    Serial.println();
    rf4463.rxInit();
  }
}