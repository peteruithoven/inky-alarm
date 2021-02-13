#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import time
import copy
import pytz
from os import path
from datetime import datetime
from sys import exit
from pathlib import Path
from font_fredoka_one import FredokaOne
from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont
import icon_map
from mask import create_mask
from weather import get_weather

alarm_path = str(Path.home()) + "/alarm.txt"
alarm = open(alarm_path,'r').read()
print("alarm: " + alarm)

PATH = path.dirname(__file__) # Current path
API_KEY = open(path.join(PATH,"key.txt"),'r').read().strip()
UNITS = "metric"
LAT = 52.377956
LON = 4.897070

# path = str(Path.home()) + "/alarms.json"
# now = datetime.now()
# next_alarm_time = "";
# with open(path, "r") as json_file:
#     alarms = json.load(json_file)
#     enabled_alarms = filter(lambda alarm: alarm['enabled'], alarms)
#     enabled_alarms

# sorted_alarms = sorted(random, key=take_second)

#     for alarm in enabled_alarms:
#         print('enabled: ' + str(alarm['enabled']))
#         hours = alarm['time']["hours"]
#         minutes = alarm['time']["minutes"]
#         print('time: ' + str(hours) + ':' + str(minutes))
#         # print('days: ' + ",".join(alarm['days']))
#         print('')
#         # if (alarm['enabled'] and
#         #     hours >= now.hour and
#         #     minutes >= now.minute):
#             #now.weekday() in alarm['days']
#         if (alarm['enabled']):
#             print("is next alarm")
#             next_alarm_time = '{}:{:0>2}'.format(hours, minutes)
#             print("next_alarm_time: " + next_alarm_time);

# enabled_alarms = filter(lambda alarm: alarm['enabled'])

def convert(img):  # 8 bit indexed color image (white, black, red)
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0))
    return img.convert("RGB").quantize(palette=pal_img)

weather = get_weather(LAT, LON, UNITS, API_KEY)

# Set up the display
try:
    inky_display = auto(ask_user=True, verbose=True)
    # inky_display = InkyPHAT("black")
except TypeError:
    raise TypeError("You need to update the Inky library to >= v1.1.0")

if inky_display.resolution not in ((212, 104), (250, 122)):
    w, h = inky_display.resolution
    raise RuntimeError("This example does not support {}x{}".format(w, h))

inky_display.set_border(inky_display.WHITE)

# Create a new canvas to draw on
img = Image.new("P", inky_display.resolution)
draw = ImageDraw.Draw(img)

# Fonts
bottom_bar_font = ImageFont.truetype(FredokaOne, 16)
temp_font = ImageFont.truetype(FredokaOne, 50)
minmax_font = ImageFont.truetype(FredokaOne, 20)

# Weather icon
icon_map = icon_map.night if weather.night else icon_map.general
icon_path = path.join(PATH, "icons/wi-" + icon_map[weather.id])
print("icon file: ", icon_path)
icon_image = convert(Image.open(icon_path))
mask = create_mask(icon_image)

icon_x = 30
icon_y = -5
if icon_image is not None:
    img.paste(icon_image, (icon_x, icon_y), mask)
else:
    draw.text((icon_x, icon_y), "?", inky_display.YELLOW, font=temp_font)

# temperatures
draw.text((137, 5), u"{}°".format(weather.temp), inky_display.BLACK, font=temp_font)
draw.text((137, 55), u"{}° | {}°".format(weather.temp_min, weather.temp_max), inky_display.BLACK, font=minmax_font)

# Bottom bar
top_padding = 4
padding = 8
datetime = time.strftime("%H:%M  %d %b")
datetime_w, datetime_h = bottom_bar_font.getsize(datetime)
datetime_x = padding
datetime_y = int(inky_display.height - datetime_h - padding)

alarm_w, alarm_h = bottom_bar_font.getsize(alarm)
alarm_x = inky_display.width - alarm_w
alarm_y = int(inky_display.height - alarm_h - padding)

# Yellow bar
for y in range(int(datetime_y-top_padding), inky_display.height):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.YELLOW)

draw.text((datetime_x, datetime_y), datetime, inky_display.BLACK, font=bottom_bar_font)

draw.text((alarm_x, alarm_y), alarm, inky_display.BLACK, font=bottom_bar_font)

img = img.rotate(180)

# Display on Inky pHAT
inky_display.set_image(img)
inky_display.show()
