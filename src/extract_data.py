import requests
import json
from pathlib import Path

def extract_weather_data(url:str) -> list:
    response = requests.get(url)
    data = response.json()

    