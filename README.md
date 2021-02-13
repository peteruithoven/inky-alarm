# inky-alarm
DIY Pi Zero alarm with Inky pHat

## Setup

### Crontab
```
*/30 * * * * python3 /home/pi/inky-alarm/display/display.py
* * * * * python3 /home/pi/inky-alarm/alarm/alarm.py
```

## webserver service
- Install a recent Node.js for armv6l
- Run server on port 80 by adding the following lines before the exit line in `/etc/rc.local`:
  ```
  # Forward port 80 to 3000 (where our web server is) so the
  # web server can run at normal permissions
  iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 3000
  ```
- Move `alarm-webapp/alarm-webapp.service` to `/etc/systemd/system/`
