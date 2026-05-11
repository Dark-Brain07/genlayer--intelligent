# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class NumberFactOracle(gl.Contract):
    """
    Chain Quest: City Lore Oracle
    Fetches REAL geographic data about cities worldwide
    from the Open-Meteo Geocoding API (proven HTTPS)
    to generate dungeon location names and elevation-based difficulty.
    """
    last_city: str
    last_elevation: str

    def __init__(self):
        self.last_city = ""
        self.last_elevation = "0"

    @gl.public.write
    def fetch_city_lore(self, city_name: str) -> str:
        if city_name == "":
            city_name = "London"

        url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city_name + "&count=1&language=en&format=json"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            results = data.get("results", [])
            if len(results) > 0:
                city = results[0]
                name = city.get("name", "Unknown")
                country = city.get("country", "Unknown")
                elevation = str(city.get("elevation", 0))
                lat = str(city.get("latitude", 0))
                lon = str(city.get("longitude", 0))
                return name + "|" + country + "|" + elevation + "|" + lat + "|" + lon
            return "Unknown|Unknown|0|0|0"

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_city = parts[0] + ", " + parts[1]
        self.last_elevation = parts[2]
        return "Dungeon Location: " + parts[0] + ", " + parts[1] + " | Elevation: " + parts[2] + "m | Coords: " + parts[3] + ", " + parts[4]

    @gl.public.view
    def get_last_city(self) -> str:
        return self.last_city

    @gl.public.view
    def get_elevation(self) -> str:
        return self.last_elevation
