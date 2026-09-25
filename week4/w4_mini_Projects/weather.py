"""
4. Weather App using OpenWeather API

SETUP REQUIRED before running:
1. Sign up (free) at https://openweathermap.org/api
2. Get your API key from https://home.openweathermap.org/api_keys
   (note: newly created keys can take a few minutes to a couple of
   hours to activate)
3. Install the requests library if you don't have it:
       pip install requests
4. Paste your API key into API_KEY below, OR enter it when prompted.
"""

import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # <-- replace with your key


def get_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Could not fetch weather data')}")
        return

    print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
    print(f"Condition: {data['weather'][0]['description'].title()}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels like: {data['main']['feels_like']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind speed: {data['wind']['speed']} m/s")


def main():
    api_key = API_KEY
    if api_key == "YOUR_OPENWEATHERMAP_API_KEY":
        api_key = input("Enter your OpenWeatherMap API key: ")

    city = input("Enter city name: ")
    get_weather(city, api_key)


if __name__ == "__main__":
    main()