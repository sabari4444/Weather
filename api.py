import json
from urllib.request import urlopen





def api_re_load():
    global location, humidity, uv, temp, w_speed, w_pressure, rain_hr, w_day, ip_ad, data, data1
    url1 = "https://ipinfo.io/json"
    response1 = urlopen(url1)
    data = json.load(response1)
    ip_ad = (data['ip'])
    city = data['city']
    state = data['region']
    country = data['country']
    postal = data['postal']
    service_provider = data['org']
    location = city + ', ' + state
    api_key = "ac1dc9e8c2e945deb3e102426223004"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ip_ad}&aqi=yes"
    response = urlopen(url)
    data1 = json.load(response)
    current = data1 ['current']
    w_condition = current['condition']
    w_day = w_condition['text']
    w_degree = current['wind_degree']
    w_speed = current["wind_kph"]
    w_pressure = current["pressure_mb"]
    rain_hr = current["precip_mm"]
    humidity = current["humidity"]
    uv = current["uv"]
    temp = round(current['temp_c'])
    #max_temp = round(w_condition)
def prnt():
    print(data)
    print(data1)
    print(ip_ad)
    print(location)
    print(humidity)
    print(uv,temp,w_speed,w_pressure,rain_hr,w_day)

api_re_load()

if __name__ == "__main__":
    prnt()