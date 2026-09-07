
import requests

def get_current_weather(city, country=None):
    """
    Obtiene el clima actual para una ciudad y país opcional usando wttr.in.
    Retorna una cadena con la temperatura y la descripción.
    """
    location = f"{city},{country}" if country else city
    url = f"https://wttr.in/{location}?format=%t+%C"
    try:
        headers = {'User-Agent': 'curl/7.64.1'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.text.strip()
        if "Unknown location" in data or not data:
            return f"Lo siento, no pude encontrar información para '{location}'."
        return f"Clima actual en {city.capitalize()}: {data}"
    except requests.exceptions.RequestException:
        return "Hubo un error de conexión al consultar el servicio de clima. Por favor, intenta más tarde."
