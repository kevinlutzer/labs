#include <RF4463.h>
#include <SPI.h>
#include <Wire.h>

#define TX_LED A0 // PD3 -> D14
#define RX_LED A6 // PD5 -> D20
#define TRIG 3

RF4463 rf4463;
unsigned char tx_buf[]={"swwxABCDEFGHIm"};
unsigned char val;

bool tx_led_status = 0;
bool rx_led_status = 0;

void changeLEDStatus() {
  tx_led_status = !tx_led_status;
  rx_led_status = !rx_led_status;
  Serial.println("\n rx led: ");
  Serial.print(rx_led_status, DEC);
  Serial.println("\n tx led: ");
  Serial.print(tx_led_status, DEC);
}

void setup() {
  Wire.begin(4);
  Serial.begin(9600);

  Serial.println("Starting connection...");

  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(TX_LED, OUTPUT);
  pinMode(RX_LED, OUTPUT);

  digitalWrite(LED_BUILTIN, HIGH);

  if(!rf4463.init())
    Serial.println("Init fail!");
  
  rf4463.enterStandbyMode();
  attachInterrupt(digitalPinToInterrupt(TRIG), changeLEDStatus, CHANGE);
}

void receiveEvent(int howMany)

{
  Serial.println("Recieved Data! Size is: ");
  Serial.print(howMany, DEC);

  while(1 < Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    Serial.print(c);         // print the character
  }

  int x = Wire.read();    // receive byte as an integer

  Serial.println(x);         // print the integer
  Wire.onRequest(receiveEvent);
}

void loop() 
{
    digitalWrite(LED_BUILTIN, HIGH);

    digitalWrite(TX_LED, tx_led_status);
    digitalWrite(RX_LED, rx_led_status);

    val=Serial.read();  // please make sure serial is OK befor runing this code
    if(val=='T') {    // tx a packet if receive "T"
      rf4463.txPacket(tx_buf,sizeof(tx_buf));
      Serial.println("tx");
      rf4463.enterStandbyMode();      // go to sleep till next tx
    }
}