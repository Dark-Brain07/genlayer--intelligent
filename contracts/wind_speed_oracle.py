# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class WindSpeedOracle(gl.Contract):
    """
    Chain Quest: Wind Speed Oracle
    Fetches REAL wind speed data from Open-Meteo
    to determine sailing and flight mechanics.
    """
    last_wind_speed: str
    last_direction: str

    def __init__(self):
        self.last_wind_speed = "0"
        self.last_direction = "0"

    @gl.public.write
    def fetch_wind_data(self, lat: str, lon: str) -> str:
        url = "https://api.open-meteo.com/v1/forecast?latitude=" + lat + "&longitude=" + lon + "&current_weather=true"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            wind_speed = str(data["current_weather"]["windspeed"])
            wind_direction = str(data["current_weather"]["winddirection"])
            return wind_speed + "|" + wind_direction

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_wind_speed = parts[0]
        self.last_direction = parts[1]
        return "Wind: " + parts[0] + " km/h | Direction: " + parts[1] + " deg"

    @gl.public.view
    def get_wind_speed(self) -> str:
        return self.last_wind_speed
