# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class ISSTrackerOracle(gl.Contract):
    """
    Chain Quest: Ocean Explorer Oracle
    Fetches REAL ocean & marine weather data from Open-Meteo Marine API
    to generate sea-themed dungeon environments and wave mechanics.
    Uses the proven Open-Meteo HTTPS infrastructure for reliable consensus.
    """
    last_wave_height: str
    last_wave_direction: str

    def __init__(self):
        self.last_wave_height = "0"
        self.last_wave_direction = "0"

    @gl.public.write
    def fetch_ocean_data(self, lat: str, lon: str) -> str:
        if lat == "":
            lat = "54.33"
        if lon == "":
            lon = "10.13"

        url = "https://marine-api.open-meteo.com/v1/marine?latitude=" + lat + "&longitude=" + lon + "&current=wave_height,wave_direction,wave_period"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            current = data["current"]
            wave_height = str(current["wave_height"])
            wave_direction = str(current["wave_direction"])
            wave_period = str(current["wave_period"])
            return wave_height + "|" + wave_direction + "|" + wave_period

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_wave_height = parts[0]
        self.last_wave_direction = parts[1]
        return "Ocean Data: Wave " + parts[0] + "m | Direction: " + parts[1] + "° | Period: " + parts[2] + "s"

    @gl.public.view
    def get_wave_height(self) -> str:
        return self.last_wave_height

    @gl.public.view
    def get_wave_direction(self) -> str:
        return self.last_wave_direction
