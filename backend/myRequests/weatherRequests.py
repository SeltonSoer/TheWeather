import requests
import os
import json

class Weather:

    api_key = os.getenv('API_WEATHER_KEY')

    def get_weather(self, city):
        request = requests.get(f'http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}')

        if request.status_code == 200:
            data = request.json()

            formatted_weather_info = json.dumps(data, indent=4, ensure_ascii=False)
            print(formatted_weather_info)

            return data['current']
        else:
            print(request)
