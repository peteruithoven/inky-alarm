import board
from datetime import datetime
from adafruit_ht16k33.segments import Seg7x4

i2c = board.I2C()
display = Seg7x4(i2c, address=0x70)

now = datetime.now() # current date and time

daytime = now.hour > 7 and now.hour < 19
display.brightness = 0.4 if daytime else 0

time = now.strftime("%H:%M")

display.print(time)
