# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class DogFactOracle(gl.Contract):
    """
    Chain Quest: Dog Fact Oracle
    Fetches REAL random dog facts to generate
    companion pet dialogue and lore text.
    """
    last_fact: str

    def __init__(self):
        self.last_fact = ""

    @gl.public.write
    def fetch_dog_fact(self) -> str:
        url = "https://dogapi.dog/api/v2/facts?limit=1"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = response.json()
            fact = data["data"][0]["attributes"]["body"]
            return fact

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_fact = result
        return "Pet Lore: " + result

    @gl.public.view
    def get_last_fact(self) -> str:
        return self.last_fact
