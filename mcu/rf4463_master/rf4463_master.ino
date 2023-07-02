#include <RF4463.h>
#include <SPI.h>
#include <Wire.h>

// rf4463_master.pde

// Caution:RF4463 can only work under 3.3V
// please make sure the supply of you board is under 3.3V
// 5v supply will destroy RF4463 module!!

// This code runs in master mode and  works with rf4463_slave.pde 
// Flow:receive "T" from serial->send a packet->wait for reply
// data of packet is "swwxABCDEFGHIm"

#include <RF4463.h>
#include <SPI.h>

#define IRQ 2
#define SDN 9 // 
#define SEL 10 // 

RF4463 rf4463 = RF4463(IRQ, SDN, SEL);
unsigned char tx_buf[]={"Hello World"};
unsigned char val;
unsigned char flag=0;    //  flag of rx mode
unsigned char rx_len;
unsigned char rx_buf[20];
uint8_t count = 0;

void setup() {
  Serial.begin(9600);

  if(!rf4463.init())
    Serial.println("Init fail!");
  else
    Serial.println("Init success!");


  if(!rf4463.setTxPower(127))
    Serial.println("Failed to set power to max!");
}

void loop() {
  rf4463.txPacket(tx_buf,sizeof(tx_buf));

  Serial.println("tx ");
  Serial.print(count, DEC);
  Serial.println("\n");
  count += 1;

  delay(10);
}
