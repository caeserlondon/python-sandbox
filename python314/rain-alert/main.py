import requests

api_key = "caddd2fda8646ad185f11b2d8042d4c0"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)
