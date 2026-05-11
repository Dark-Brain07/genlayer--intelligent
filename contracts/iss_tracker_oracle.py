# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class ISSTrackerOracle(gl.Contract):
    """
    Chain Quest: ISS Tracker Oracle
    Fetches REAL International Space Station position
    to generate space-themed dungeon coordinates.
    """
    last_latitude: str
    last_longitude: str

    def __init__(self):
        self.last_latitude = "0"
        self.last_longitude = "0"

    @gl.public.write
    def fetch_iss_position(self) -> str:
        url = "http://api.open-notify.org/iss-now.json"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = response.json()
            lat = data["iss_position"]["latitude"]
            lon = data["iss_position"]["longitude"]
            return lat + "|" + lon

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_latitude = parts[0]
        self.last_longitude = parts[1]
        return "ISS at Lat: " + parts[0] + " Lon: " + parts[1]

    @gl.public.view
    def get_iss_lat(self) -> str:
        return self.last_latitude
