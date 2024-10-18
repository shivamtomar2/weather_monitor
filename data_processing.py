def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    main = data['main']
    weather = data['weather'][0]
    temperature_c = kelvin_to_celsius(main['temp'])
    feels_like_c = kelvin_to_celsius(main['feels_like'])
    weather_condition = weather['main']
    return temperature_c, feels_like_c, weather_condition
