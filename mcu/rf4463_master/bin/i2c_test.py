# <keyword data-keyword-id="246">Raspberry Pi</keyword> to Arduino I2C Communication
# Python Code
 
import smbus
 
# Slave Addresses for Arduinos
ARDUINO_1_ADDRESS = 0x04 # I2C Address of Arduino 1
ARDUINO_2_ADDRESS = 0x05 # I2C Address of Arduino 2
ARDUINO_3_ADDRESS = 0x06 # I2C Address of Arduino 3

# This function converts a string to an array of bytes.
def ConvertStringToBytes(src):
  if src == "1":
    src = "on"
  else:
    src == "off"

  converted = []
  for b in src:
    converted.append(ord(b))
 
  return converted
 
# Create the I2C bus
I2Cbus = smbus.SMBus(1)
 
bSelect = input("On or Off (1/0): ")
 
SlaveAddress = ARDUINO_1_ADDRESS
 
# also quit if you messed up
# if bSelect != "0" or bSelect != "1": quit()

BytesToSend = ConvertStringToBytes("off")
I2Cbus.write_i2c_block_data(0x04, 0x00, BytesToSend)

