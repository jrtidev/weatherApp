import requests
import json
from meteocalc import Temp, dew_point, heat_index

url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,ua&appid=%s'
key = '65e35748bfe2f7d0e48946797b374b44'

    
def get_weather(url, key):
    city = raw_input('Input city: ')
    r = requests.get(url % (city, key))
    json_r = r.json()
    temp_kel = json_r['main']['temp']
    precipitation = json_r['weather'][0]['description']
    wind = json_r['wind']['speed']
    temp_cel = round(temp_kel-273.15)
    humidity=json_r['main']['humidity']
    t = Temp(temp_cel, 'c')
    hi = heat_index(temperature=t, humidity=humidity)



    print("Current temperature in "+city+' : ' + str(temp_cel))  
    print ("Precipitation: "+precipitation)
    print ("Wind speed: %s meters per second" % wind)
    print ("Humidity: %s" % str(humidity)+'%')
    print ("Feel\'s like: %s" % str(round((hi.c)))+'C')
    print ('==========================================')
    

while True:
    get_weather(url, key)
