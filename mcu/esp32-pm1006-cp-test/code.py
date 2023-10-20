import board
import digitalio
import busio
import time
from analogio import AnalogIn


uart = busio.UART(tx=board.IO5, rx=board.IO4, baudrate=9600)
i2c = busio.I2C(board.IO6, board.IO7)
pd_in = AnalogIn(board.IO3)

FAN = board.IO10

def pm1006_ping():

    print(FAN)
    pin = digitalio.DigitalInOut(FAN)
    pin.direction = digitalio.Direction.OUTPUT

    pin.value = True

    while True:
        time.sleep(1)
        print(uart.write(bytearray(b'.\x11\x02\x0b\x01\xe1')))
        print(uart.read(16))

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

pm1006_ping()
