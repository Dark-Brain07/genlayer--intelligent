# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class ISSTrackerOracle(gl.Contract):
    """
    Chain Quest: Space Data Oracle
    Fetches REAL solar system planetary data from Le Systeme Solaire API
    to generate space-themed dungeon attributes and gravity mechanics.
    Uses deterministic planetary data for reliable validator consensus.
    """
    last_planet: str
    last_gravity: str

    def __init__(self):
        self.last_planet = ""
        self.last_gravity = "0"

    @gl.public.write
    def fetch_planet_data(self, planet: str) -> str:
        if planet == "":
            planet = "mars"
        
        planet = planet.lower()

        url = "https://api.le-systeme-solaire.net/rest/bodies/" + planet

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            name = data["englishName"]
            gravity = str(data["gravity"])
            mass_value = str(data["mass"]["massValue"])
            return name + "|" + gravity + "|" + mass_value

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_planet = parts[0]
        self.last_gravity = parts[1]
        return "Planet: " + parts[0] + " | Gravity: " + parts[1] + " m/s² | Mass: " + parts[2]

    @gl.public.view
    def get_planet(self) -> str:
        return self.last_planet

    @gl.public.view
    def get_gravity(self) -> str:
        return self.last_gravity
