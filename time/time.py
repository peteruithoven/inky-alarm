import time
from datetime import datetime
import board
import busio
from adafruit_ht16k33.segments import Seg7x4

i2c = busio.I2C(board.SCL, board.SDA)
display = Seg7x4(i2c, address=0x70)

now = datetime.now() # current date and time

daytime = 7 < now.hour < 19
display.brightness = 0.4 if daytime else 0.0

time = now.strftime("%H:%M")

display.print(time)
