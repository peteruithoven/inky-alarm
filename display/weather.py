import requests
import json

class Weather:
    def __init__(self, id, temp, min, max, clouds, night ):
        self.id = id
        self.temp = round(temp)
        self.temp_min = round(min)
        self.temp_max = round(max)
        self.clouds = clouds
        self.night = night

def get_weather(lat, lon, units, api_key):
    url = "https://api.openweathermap.org/data/3.0/onecall?lat=%s&lon=%s&units=%s&exclude=hourly,minutely&appid=%s" % (
    lat, lon, units, api_key)
    res = requests.get(url)
    if res.status_code == 200:
        data = json.loads(res.text)
        current = data["current"]
        id = current["weather"][0]["id"]
        temp = current["temp"]
        clouds = current["clouds"]
        today = data["daily"][0]
        temp_min = today["temp"]["min"]
        temp_max = today["temp"]["max"]
        # night = current["dt"] > current["sunset"]
        night = current["dt"] > current["sunset"] or current["dt"] < current["sunrise"]
        print("id: " + str(id))
        print("description: " + str(current["weather"][0]["description"]))
        print("temp: " + str(temp))
        print("temp_min: " + str(temp_min))
        print("temp_max: " + str(temp_max))
        print("night: " + str(night))
        return Weather(id, temp, temp_min, temp_max, clouds, night)
    else:
        print("Weather request failed")
        exit()
