# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class ISSTrackerOracle(gl.Contract):
    """
    Chain Quest: Space Data Oracle (Powered by NASA)
    Fetches REAL daily astronomy data from NASA's APOD API
    to generate space-themed dungeon lore and events.
    Uses NASA's official stable API for reliable consensus.
    """
    last_title: str
    last_date: str

    def __init__(self):
        self.last_title = ""
        self.last_date = ""

    @gl.public.write
    def fetch_nasa_data(self) -> str:
        # NASA's official public demo API key
        url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            # Extract stable fields: Title and Date
            title = data["title"]
            date = data["date"]
            return title + "|" + date

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_title = parts[0]
        self.last_date = parts[1]
        return "NASA Update: " + parts[0] + " (" + parts[1] + ")"

    @gl.public.view
    def get_space_title(self) -> str:
        return self.last_title

    @gl.public.view
    def get_space_date(self) -> str:
        return self.last_date
