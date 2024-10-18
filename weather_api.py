import requests

API_KEY = 'c665a90bd3a5162d97c1960542c95f90'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    response = requests.get(API_URL, params={'q': city, 'appid': API_KEY})
    return response.json()
