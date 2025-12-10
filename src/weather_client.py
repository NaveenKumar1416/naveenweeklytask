import requests
from typing import Optional, Dict
from .config import OPENWEATHER_API_KEY, UNITS

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_for_city(city: str) -> Optional[Dict]:
    """Fetch weather data for a single city from OpenWeather."""
    try:
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": UNITS,
        }
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "conditions": data["weather"][0]["description"],
        }
    except Exception as e:
        print(f"[ERROR] Failed to fetch data for {city}: {e}")
        return None

