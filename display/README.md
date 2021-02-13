# Inky pHAT display with weather info

Inky pHAT eInk display from Pimoroni driven by a Raspberry Pi Zero (or any other Raspberry Pi) to display current weather

Icons are from Erik Flowers:

[Weather Icons](https://github.com/erikflowers/weather-icons)

The weather information is fetched from OpenWeather:

[OpenWeather](https://openweathermap.org)

Here you need to create an account and an API key. Put the code into a "key.txt" file. You also need to set your location ("lat" and "lon" variables).

## Setup

The Pimoroni Inky pHAT display requires a bunch of software to be installed. My recommendation is to follow the description in a Pimoroni tutorial:

[Getting Started with Inky pHAT](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat)

The installation is done by executing a bash script, and it takes a while. Everything is installed for Python 2 and 3 which isn't necessary from my point of view, so you might consider deselecting version 2 in the script before running it.

We need to convert Erik's SVG icons to 8 bit PNGs. I'm using the Imagemagick "mogrify" command for the bulk convert. With Erik's original SVGs this would deliver PNGs with a 30 x 30 pixel resolution which is too small. Using the mogrify's "resize" option didn't work so I changed the SVGs to 95 x 95 pixels by using a "vim" script (see below). The original SVGs are stored in a 7z-file in the "icons" folder. In the setup script "setup.sh" there is a line to remove the modified SVGs after PNG conversion (commented out, security reasons ;-) ).

The main Python file to drive the display is "weather.py". My display is a "red" one. You may have to change the color in the Python file if you own a different one.

Here is what the setup script "setup.sh" does:

```
cd icons
7za x erik_flowers_weather-icons.7z
find -name "*.svg" -exec vim -s script.vim {} \;
mogrify -background white -format PNG8 *.svg
#rm *.svg
```

## Credit

* The icons are provided by Erik Flowers.
* Big part of approach is inspired by [Inky wHAT Weather Station](https://github.com/rbunger/Inky-wHAT-Weather-Station) made by Rainer Bunger.

## Licensing

The weather icons and the font are licensed under [SIL OFL 1.1](http://scripts.sil.org/OFL).
