# inky-alarm
DIY Pi Zero alarm with Inky pHat

## Setup

### Crontab
```
*/30 * * * * python3 /home/pi/inky-alarm/display/display.py
* * * * * python3 /home/pi/inky-alarm/alarm/alarm.py
```

## webserver service
Move `alarm-webapp/alarm-webapp.service` to `/etc/systemd/system/`
