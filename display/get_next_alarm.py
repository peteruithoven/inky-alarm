#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from datetime import datetime
from pathlib import Path
import json

def get_next_alarm():
  path = str(Path.home()) + "/alarms.json"
  now = datetime.now()
  # print("now:", now.strftime("%m/%d/%Y, %H:%M:%S"))
  with open(path, "r") as json_file:
    alarms = json.load(json_file)
    enabled_alarms = filter(lambda alarm: alarm['enabled'], alarms)

    next_alarms = []
    for alarm in enabled_alarms:
      hours = alarm['time']["hours"]
      minutes = alarm['time']["minutes"]
      weekdays = alarm['days']
      # print('- ' + str(hours) + ":" + str(minutes) + ' ' + ','.join(map(str,weekdays)))

      for weekday_delta in range(7):
        weekday = (now.weekday()+weekday_delta)%7
        if(weekday in weekdays and
          ((now.hour < hours and
          now.minute < minutes) or weekday_delta > 0)):
            sortable = weekday_delta*100 + hours*10, minutes
            next_alarms.append([sortable, weekday, hours, minutes])
    next_alarms.sort(key=lambda elem: elem[0])
    # print("alarms:")
    # for alarm in next_alarms:
    #   weekday_name = weekday_names[alarm[1]]
    #   print("    {} {}:{}".format(weekday_name, alarm[2], alarm[3]))
    next_alarm = next_alarms[0]
    sortable, weekday, hour, minute = next_alarm
    return weekday, hour, minute



