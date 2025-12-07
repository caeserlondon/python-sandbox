# import requests
# import os
#
# # api_key1 = "caddd2fda8646ad185f11b2d8042d4c0"
# api_key2 = os.environ.get("OWM_API_KEY")
# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
# weather_params = {
#     "lat": 51.507351,
#     "lon": -0.127758,
#     "appid": api_key2,
# }
#
# response = requests.get(OWM_Endpoint, params=weather_params)
# # response.raise_for_status()
# data = response.json()
#
# # print(data)
#
# print(api_key2)
# print(response.status_code)

import os
print(os.getenv("OWM_API_KEY"))
