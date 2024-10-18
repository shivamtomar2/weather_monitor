import unittest
from src.weather_api import get_weather_data

class TestWeatherAPI(unittest.TestCase):
    def test_get_weather_data(self):
        data = get_weather_data('Delhi')
        self.assertIn('main', data)
        self.assertIn('weather', data)

if __name__ == '__main__':
    unittest.main()
