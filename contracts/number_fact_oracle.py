# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class NumberFactOracle(gl.Contract):
    """
    Chain Quest: Number Trivia Oracle
    Fetches REAL number trivia from NumbersAPI
    to generate riddle puzzles for dungeon gates.
    """
    last_trivia: str

    def __init__(self):
        self.last_trivia = ""

    @gl.public.write
    def fetch_number_trivia(self, number: str) -> str:
        url = "http://numbersapi.com/" + number + "/trivia?json"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.text)
            trivia = data["text"]
            return trivia

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_trivia = result
        return "Riddle: " + result

    @gl.public.view
    def get_last_trivia(self) -> str:
        return self.last_trivia
