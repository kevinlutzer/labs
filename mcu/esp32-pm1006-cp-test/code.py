import board
import digitalio
import busio
import time

FAN = board.IO10

print(FAN)
pin = digitalio.DigitalInOut(FAN)
pin.direction = digitalio.Direction.OUTPUT

pin.value = True

uart = busio.UART(tx=board.IO5, rx=board.IO4, baudrate=9600)
while True:
    time.sleep(1)
    print(uart.write(bytearray(b'.\x11\x02\x0b\x01\xe1')))
    print(uart.read(8))
