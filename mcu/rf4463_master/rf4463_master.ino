// rf4463_master.pde

// Caution:RF4463 can only work under 3.3V
// please make sure the supply of you board is under 3.3V
// 5v supply will destroy RF4463 module!!

// This code runs in master mode and  works with rf4463_slave.pde 
// Flow:receive "T" from serial->send a packet->wait for reply
// data of packet is "swwxABCDEFGHIm"

#include "RF4463.h"
#include <SPI.h>

RF4463 rf4463;

void setup() {

  Serial.begin(9600);

  rf4463.pinInit();
	rf4463.spiInit();
  rf4463.powerOnReset();

  while(!rf4463.checkDevice()) {
    Serial.println("Init FAILLLL!");
    delay(1000);
  }

  Serial.println("init Success");

  rf4463.enterStandbyMode();
}
void loop() {}