# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Example for Pico. Turns on the built-in LED."""
import board
from digitalio import DigitalInOut, Direction
from busio import SPI
from sdcardio import SDCard
from storage import VfsFat, mount
import time
# from os.path import getsize
import os
# led
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

# spi
spi = SPI(board.GP18, board.GP19, board.GP16)

sd = SDCard(spi, board.GP17)
vfs = VfsFat(sd)
mount(vfs, '/sd')

base = "X6}-}Le4YhcGhiD2383yWC&w$m9,,Pwv+QpdEyh3&:K&*3Bt6jX]bb8c!X-R8_RP$hX[cS,$-Y;?3mbFPcLw_ZM92pv2WexRdi?St@:4DeF%)"

# print(dir(os.stat('/sd/test.txt').st_size))
# print('file size: ', getsize('/sd/test.txt'))

final_str = ""
for _ in range(0, 60):
	final_str = final_str + base

while True:
	f = open("/sd/test.txt", "a+")
	print(os.stat('/sd/test.txt'))

	f.write(final_str)
	f.flush()
	f.close()