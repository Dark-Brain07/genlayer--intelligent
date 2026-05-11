# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class UniversityOracle(gl.Contract):
    """
    Chain Quest: University Oracle
    Fetches REAL university data from Hipolabs API
    to generate scholar NPC backgrounds and academy quests.
    """
    last_university: str
    last_country: str

    def __init__(self):
        self.last_university = ""
        self.last_country = ""

    @gl.public.write
    def fetch_university(self, country: str) -> str:
        url = "http://universities.hipolabs.com/search?country=" + country + "&limit=1"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.text)
            if len(data) > 0:
                name = data[0]["name"]
                ctry = data[0]["country"]
                return name + "|" + ctry
            return "Unknown|Unknown"

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_university = parts[0]
        self.last_country = parts[1]
        return "Academy: " + parts[0] + " | Kingdom: " + parts[1]

    @gl.public.view
    def get_university(self) -> str:
        return self.last_university
