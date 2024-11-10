from myRequests.weatherRequests import Weather

def main():
    weather = Weather()
    weather.get_weather('Moscow')

if __name__ == '__main__':
    main()
