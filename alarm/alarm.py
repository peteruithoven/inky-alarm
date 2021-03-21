#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from datetime import datetime, timedelta
from time import time, sleep
from pathlib import Path
import json

duration = 60 # seconds
vibrate_duration = 0.1
wait_duration = 1.5
shaker_pin = 5
button_pin = 6

path = str(Path.home()) + "/alarms.json"
with open(path, "r") as json_file:
    alarms = json.load(json_file)
    for alarm in alarms:
        print('enabled: ' + str(alarm['enabled']))
        hours = alarm['time']["hours"]
        minutes = alarm['time']["minutes"]
        print('time: ' + str(hours) + ':' + str(minutes))
        # print('days: ' + ",".join(alarm['days']))
        print('')

GPIO.setmode(GPIO.BCM)
GPIO.setup(shaker_pin, GPIO.OUT)
GPIO.output(shaker_pin, False)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # using the internal Pull up resistor

def is_alarm_time():
  now = datetime.now()
  for alarm in alarms:
    # print("enabled: " + str(alarm['enabled']))
    # print("hours match: " + str(now.hour == alarm['time']["hours"]))
    # print("minutes match: " + str(now.minute == alarm['time']["minutes"]))
    # print("weekday match: " + str(now.weekday() in alarm['days']))
    if (alarm['enabled'] and
        now.hour == alarm['time']["hours"] and
        now.minute == alarm['time']["minutes"] and
        now.weekday() in alarm['days']):
        # print("alarm time")
        return True
  return False

vibrate = True
if is_alarm_time():
  start_time = toggle_time = time()
  while time() < start_time+duration:
    if time() >= toggle_time:
      print("vibrate: " + str(vibrate))
      GPIO.output(shaker_pin, not vibrate)
      vibrate = not vibrate
      toggle_time = time()+(vibrate_duration if vibrate else wait_duration)
    if not GPIO.input(button_pin):
      break
    # print("button: ", str(GPIO.input(button_pin)));
    sleep(0.1)

GPIO.output(shaker_pin, False)
GPIO.cleanup()
