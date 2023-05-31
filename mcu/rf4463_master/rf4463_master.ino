//Arduino code to receive I2C communication from <keyword data-keyword-id="247">Raspberry Pi</keyword>
 
#include <Wire.h>
 
// Define the slave address of this device.
#define SLAVE_ADDRESS 0x20
// #define SLAVE_ADDRESS 0x05
// #define SLAVE_ADDRESS 0x06
 
// string to store what the RPi sends
String str_recieved_from_RPi = "";
 
void setup() {

Serial.begin(9600);
 
// setup the LED
pinMode(LED_BUILTIN, OUTPUT);
 
// begin running as an I2C slave on the specified address
Wire.begin(0x20);

// create event for receiving data
Wire.onReceive(receiveData);
Serial.println("Started");
}
 
void loop() {
  // Wire.beginTransmission(0x04);cd r
  // Wire.write(0x01);
  // Wire.endTransmission();

  // delay(100);
}
 
void receiveData(int byteCount) {
 
Serial.println("Recieve Data");

while ( Wire.available()) {
str_recieved_from_RPi += (char)Wire.read();
}
// turn on or off the LED
if (str_recieved_from_RPi == "on") {
digitalWrite(LED_BUILTIN, HIGH);
}
if (str_recieved_from_RPi == "off") {
digitalWrite(LED_BUILTIN, LOW);
}
 
str_recieved_from_RPi = "";
 
}

// #include <RF4463.h>
// #include <SPI.h>
// #include <Wire.h>

// RF4463 rf4463;
// unsigned char tx_buf[]={"swwxABCDEFGHIm"};
// unsigned char val;

// void setup() {
//   Wire.begin(4);
//   Serial.begin(9600);

//   Serial.println("Starting connection...");

//   pinMode(LED_BUILTIN, OUTPUT);
//   digitalWrite(LED_BUILTIN, HIGH);

//   if(!rf4463.init()) {
//     Serial.println("Init fail!");
//   }
  
//   rf4463.enterStandbyMode();
// }

// void receiveEvent(int howMany)

// {
//   Serial.println("Recieved Data! Size is: ");
//   Serial.print(howMany, DEC);

//   while(1 < Wire.available()) // loop through all but the last

//   {

//     char c = Wire.read(); // receive byte as a character

//     Serial.print(c);         // print the character

//   }

//   int x = Wire.read();    // receive byte as an integer

//   Serial.println(x);         // print the integer
//   Wire.onRequest(receiveEvent);
// }

// void loop() 
// {
//     digitalWrite(LED_BUILTIN, HIGH);
//     val=Serial.read();  // please make sure serial is OK befor runing this code
//     if(val=='T') {    // tx a packet if receive "T"
//       rf4463.txPacket(tx_buf,sizeof(tx_buf));
//       Serial.println("tx");
//       rf4463.enterStandbyMode();      // go to sleep till next tx
//     }
// }