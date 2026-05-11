# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class CountryInfoOracle(gl.Contract):
    """
    Chain Quest: Country Info Oracle
    Fetches REAL country data from RestCountries API
    to generate quest locations with real population and region info.
    """
    last_country: str
    last_population: str

    def __init__(self):
        self.last_country = ""
        self.last_population = "0"

    @gl.public.write
    def fetch_country_data(self, country_name: str) -> str:
        url = "https://restcountries.com/v3.1/name/" + country_name + "?fields=name,population,region,capital"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.text)
            country = data[0]
            name = country["name"]["common"]
            pop = str(country["population"])
            region = country["region"]
            return name + "|" + pop + "|" + region

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_country = parts[0]
        self.last_population = parts[1]
        return "Quest Location: " + parts[0] + " | Population: " + parts[1] + " | Region: " + parts[2]

    @gl.public.view
    def get_last_country(self) -> str:
        return self.last_country
