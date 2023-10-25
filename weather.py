import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_key = os.getenv('API_KEY')


def get_current_weather_data(country_code, city_name):
    resp = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_key}').json()
    try:
        description = resp.get('weather')[0].get('description')
        icon = resp.get('weather')[0].get('icon')
        temp = resp.get('main').get('temp')
        temp = temp - 273.15
        temp = f'{temp:.2f}°C'
        data_weather = [description, icon, temp]
    except:
        return False
    return data_weather


