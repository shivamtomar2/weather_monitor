import time
from weather_api import get_weather_data
from data_processing import process_weather_data
from db_manager import initialize_db

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def main():
    initialize_db()
    while True:
        for city in CITIES:
            data = get_weather_data(city)
            if data:
                temperature_c, feels_like_c, weather_condition = process_weather_data(data)
                print(f'Weather in {city}: {temperature_c:.2f}°C, Feels Like: {feels_like_c:.2f}°C, Condition: {weather_condition}')
        time.sleep(300)  # Wait for 5 minutes

if __name__ == '__main__':
    main()
