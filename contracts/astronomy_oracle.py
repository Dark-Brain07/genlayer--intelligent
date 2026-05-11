# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class AstronomyOracle(gl.Contract):
    """
    Chain Quest: Astronomy Oracle
    Fetches REAL astronomical data (sunrise/sunset) from Open-Meteo
    to determine day/night cycle for game events.
    """
    last_sunrise: str
    last_sunset: str

    def __init__(self):
        self.last_sunrise = ""
        self.last_sunset = ""

    @gl.public.write
    def fetch_day_cycle(self, lat: str, lon: str) -> str:
        url = "https://api.open-meteo.com/v1/forecast?latitude=" + lat + "&longitude=" + lon + "&daily=sunrise,sunset&timezone=auto&forecast_days=1"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = response.json()
            sunrise = data["daily"]["sunrise"][0]
            sunset = data["daily"]["sunset"][0]
            return sunrise + "|" + sunset

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_sunrise = parts[0]
        self.last_sunset = parts[1]
        return "Sunrise: " + parts[0] + " | Sunset: " + parts[1]

    @gl.public.view
    def get_sunrise(self) -> str:
        return self.last_sunrise
