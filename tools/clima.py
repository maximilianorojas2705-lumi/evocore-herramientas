"""Tool to fetch current weather using Open-Meteo API."""
import requests

def get_current_weather(city: str, country: str = None):
    """Return current temperature and weather description for a city.
    Uses Open-Meteo API (no key). Requires latitude and longitude.
    """
    # Geocoding via Nominatim
    geocode_url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': f"{city}{', '+country if country else ''}",
        'format': 'json',
        'limit': 1
    }
    resp = requests.get(geocode_url, params=params, headers={'User-Agent': 'evocore-tool'})
    if resp.status_code != 200 or not resp.json():
        return f"Could not find location for {city}"
    loc = resp.json()[0]
    lat = loc['lat']
    lon = loc['lon']
    # Open-Meteo API
    weather_url = 'https://api.open-meteo.com/v1/forecast'
    weather_params = {
        'latitude': lat,
        'longitude': lon,
        'current_weather': True,
        'timezone': 'auto'
    }
    wresp = requests.get(weather_url, params=weather_params)
    if wresp.status_code != 200:
        return f"Weather API error for {city}"
    data = wresp.json()
    temp = data['current_weather']['temperature']
    windspeed = data['current_weather']['windspeed']
    winddirection = data['current_weather']['winddirection']
    return f"{city}: {temp}°C, wind {windspeed} km/h from {winddirection}°"
