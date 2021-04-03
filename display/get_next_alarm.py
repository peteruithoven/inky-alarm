from os import path
from datetime import datetime, timedelta
from pathlib import Path
import json

def get_next_weekday_time(weekday, hour, minute):
    d = datetime.now()
    d = d.replace(hour=hour, minute=minute, second=0, microsecond=0)
    days_ahead = (weekday - d.weekday()) % 7
    return d + timedelta(days_ahead)

def get_next_alarm():
  now = datetime.now()
  path = str(Path.home()) + "/alarms.json"
  # print("now:", now.strftime("%a %d %b %Y, %H:%M"))
  with open(path, "r") as json_file:
    alarms = json.load(json_file)
    enabled_alarms = filter(lambda alarm: alarm['enabled'], alarms)

    next_alarms = []
    for alarm in enabled_alarms:
      hours = alarm['time']["hours"]
      minutes = alarm['time']["minutes"]
      weekdays = alarm['days']
      # print('- ' + str(hours) + ":" + str(minutes) + ' ' + ','.join(map(str,weekdays)))

      for weekday in weekdays:
        alarm_datetime = get_next_weekday_time(weekday, hours, minutes)
        if alarm_datetime > now:
          next_alarms.append(alarm_datetime)
    next_alarms.sort()

    # print("alarms:")
    # for alarm_datetime in next_alarms:
    #   print("- " + alarm_datetime.strftime("%a %d %b %Y, %H:%M"))
    return next_alarms[0]



