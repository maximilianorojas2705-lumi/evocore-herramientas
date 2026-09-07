"""Tool to fetch official and blue dollar rates from dolarapi.com.

Functions:
- get_official(): returns dict with compra, venta, fechaActualizacion
- get_blue(): same for blue
"""
import requests

BASE_URL = "https://dolarapi.com/v1/dolares"


def _fetch(tipo):
    url = f"{BASE_URL}/{tipo}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return {
        "compra": data.get("compra"),
        "venta": data.get("venta"),
        "fechaActualizacion": data.get("fechaActualizacion"),
        "nombre": data.get("nombre")
    }


def get_official():
    return _fetch("oficial")


def get_blue():
    return _fetch("blue")
