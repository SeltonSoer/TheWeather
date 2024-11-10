import requests
# import json

# 'http://api.weatherapi.com/v1/current.json?key=<YOUR_API_KEY>&q=London'

class Weather:

    # API-key add to PATH in system
    api_key = 'testKey'

    def get_weather(self, city):
        request = requests.get(f'http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}')

        if request.status_code == 200:
            data = request.json()

            # formatted_weather_info = json.dumps(data, indent=4, ensure_ascii=False)
            # print(formatted_weather_info)

            return data['current']
