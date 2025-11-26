#include <Arduino.h>
#include <SPI.h>

//
// Pins
// 

#define LED 25 // Built-in LED on Raspberry Pi Pico
#define SDN 16 // System reset for the SI4463 chip. Active low
#define IRQ 17 // IRQ Pin from the SI4463 to the Pi

#define SCK 10
#define MOSI 11
#define MISO 12 
#define CS 13

//
// CMDS
//

#define RF4463_CMD_READ_BUF                   0x44
#define RF4463_CMD_PART_INFO                  0x01

#define RF4463_CTS_REPLY					  0xff
// Waiting time for a valid FFh CTS reading
// the typical time is 20us
#define RF4463_CTS_TIMEOUT 					  2500

void powerOnReset()
{
  digitalWrite(SDN, LOW);
  delay(1000);						// wait for RF4463 stable

	// send power up command
  uint8_t tx_buf[]={0x02, 0x01, 0x00, 0x01, 0xC9, 0xC3, 0x80};
  SPI1.transfer(tx_buf, 7);

  delay(200);
}

bool checkCTS()
{
  uint16_t timeOutCnt;
	timeOutCnt=RF4463_CTS_TIMEOUT;

  Serial.println("Send request");

  uint8_t rx = 0;
  uint16_t count = 0;
  do {
    digitalWrite(CS, LOW);
    rx = SPI1.transfer(RF4463_CMD_READ_BUF);
    // digitalWrite(CS, HIGH);
    count ++;
  } while ( rx != RF4463_CTS_REPLY && count < RF4463_CTS_TIMEOUT );

  Serial.printf("RX Value received %d after count %d", rx, count);

  return rx == RF4463_CTS_REPLY;
}

bool getCommand(uint8_t length,uint8_t command, uint8_t * paraBuf) {

	Serial.printf("Command response: %d \n", SPI1.transfer(command));				// set command to read 
	
  // check if RF4463 is ready 
	if(!checkCTS())	{
    return false;  
  }

  // Serial.printf("Read Buf: %d \n", SPI1.transfer(RF4463_CMD_READ_BUF));
	// digitalWrite(CS, LOW);

  uint8_t * _txbuf = (uint8_t * ) malloc(length * sizeof(uint8_t));
  memset(_txbuf, 0x00, length);
  _txbuf[0] = RF4463_CMD_READ_BUF;

	SPI1.transfer(_txbuf, paraBuf, length);		// read parameters
	digitalWrite(CS, HIGH);

  free(_txbuf);
  return true;
}

bool checkDevice()
{
	uint8_t buf[9];
	uint16_t partInfo;

	getCommand(9, RF4463_CMD_PART_INFO, buf);		// read part info to check if 4463 works
		
  for (int i = 0; i < 9; i ++) {
    Serial.printf("Buf[%d]=%d\n", i, buf[i]);
  }

	partInfo=buf[1]<<8|buf[2];
	return partInfo == 0x4463;
}

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(SDN, OUTPUT);
	pinMode(IRQ, INPUT);

  // Disable the module on boot
  digitalWrite(SDN, HIGH);

  Serial.begin(115200); // Set baud rate
  while (!Serial);   
  Serial.println("Serial started");

  // Initialize the SPI
  SPI1.setRX(MISO);
  SPI1.setCS(CS);
  SPI1.setSCK(SCK);
  SPI1.setTX(MOSI);

  SPI1.begin(true);
  SPI1.beginTransaction(SPISettings(32768, MSBFIRST, SPI_MODE0));

  // Init the module
  powerOnReset();

  attachInterrupt(6, )

  delay(5000);

  // heck if RF4463 works
	if(!checkDevice()){
    Serial.println("Failed");
	} else {
    Serial.println("Success");
  }
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);
  delay(1000);
}