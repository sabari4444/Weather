import json
from urllib.request import urlopen
from datetime import datetime
API_key = "54bc6c33d8bf3ca30fb095839e926077"
lat = "11.1154"
lon = "77.3546"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&aqi=yes"
res = urlopen(url)
data = json.load(res)

weather= data['weather']
temp_s= data['main']

now = weather[0]
now1 = now['main']
now2 = now['description']
max_temp = temp_s['temp_max']
max_temp = round (max_temp - 273.15)
min_temp = temp_s['temp_min']
min_temp = round(min_temp -275.15)
am_pm =(datetime.today().strftime("%p"))

def prnt ():
    print(data)
    print(temp_s)
    print(max_temp)
    print(min_temp)
    print(now1)
    print(now2)

if __name__ =="__main__":
    prnt()