# inky-alarm
DIY Pi Zero alarm with Inky pHat

## Setup

### Crontab
```
$ crontab -e
*/30 * * * * /home/pi/inky-alarm/.venv/bin/python /home/pi/inky-alarm/display/display.py
* * * * * /home/pi/inky-alarm/.venv/bin/python /home/pi/inky-alarm/alarm/alarm.py
* * * * * /home/pi/inky-alarm/.venv/bin/python /home/pi/inky-alarm/time/time.py
*/5 * * * * /home/pi/inky-alarm/WiFi_Check >> ~/WiFi_Check.log
```

Optionally, have it reboot every night, to overcome common wifi issues. 
```
$ sudo crontab -e
0 4 * * *     /sbin/shutdown -r now
```

### Webserver
- Install a recent Node.js for armv6l
- Run server on port 80 by adding the following lines before the exit line in `/etc/rc.local`:
  ```
  # Forward port 80 to 3000 (where our web server is) so the
  # web server can run at normal permissions
  iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 3000
  ```
- Move `alarm-webapp/alarm-webapp.service` to `/etc/systemd/system/`
