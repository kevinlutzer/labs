import board
import digitalio
import busio
import time
from analogio import AnalogIn

import board
#from adafruit_bme280 import basic as adafruit_bme280

uart = busio.UART(tx=board.IO5, rx=board.IO4, baudrate=9600)
i2c = busio.I2C(board.IO6, board.IO7)
# bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

pd_in = AnalogIn(board.IO3)

FAN = board.IO10

def valid_header(d):
    return (d[0] == 0x16 and d[1] == 0x11 and d[2] == 0x0B)

def i2c_scanner():

    while not i2c.try_lock():
        pass

    try:
        while True:
            print(
                "I2C addresses found:",
                [hex(device_address) for device_address in i2c.scan()],
            )
            time.sleep(2)

    finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
        i2c.unlock()

def read_pd():
    pd_in
    while True:
        val = (pd_in.value * 3.3) / 65536
        print("Val: ", val)
        time.sleep(1)

measurements = []
measurement_idx = 0
while True:
    uart.write(bytearray(b'.\x11\x02\x0b\x01\xe1'))
    time.sleep(0.01)
    data = uart.read(32)
    time.sleep(0.01)
    if data is not None:
        v = valid_header(data)
        if v is True:
            measurement_idx = 0
            start_read = True
        if start_read is True:
            pm25 = (data[5] << 8) | data[6]
            measurements[measurement_idx] = pm25
            if measurement_idx == 4:
                start_read = False
            measurement_idx = (measurement_idx + 1) % 5
            print(pm25)
