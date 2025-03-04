import json
import requests


def get_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(f"Координаты МКС: {data['iss_position']}\n")


get_iss_position()

city_name = 'Komsomolsk-on-Amur'
key = '35e8e6f577a850648119f90a5ed4ce78'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)
print(result.get('name'))
print(f'Weather: {result.get("weather")[0].get("main")}')
print(f'Pressure: {result.get("main").get("pressure") // (4/3)} mmHg')
print(f'Humidity: {result.get("main").get("humidity")} %')
