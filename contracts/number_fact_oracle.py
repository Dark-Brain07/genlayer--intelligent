# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class NumberFactOracle(gl.Contract):
    """
    Chain Quest: Number & Lore Oracle
    Fetches REAL trivia and definitions from the DuckDuckGo API
    to generate riddle puzzles for dungeon gates.
    Uses a highly stable HTTPS API for reliable consensus.
    """
    last_trivia: str

    def __init__(self):
        self.last_trivia = ""

    @gl.public.write
    def fetch_number_trivia(self, query: str) -> str:
        if query == "":
            query = "42"

        # DuckDuckGo Instant Answer API (stable and returns JSON)
        url = "https://api.duckduckgo.com/?q=" + query + "&format=json"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            
            # 1. Try AbstractText
            text = data.get("AbstractText", "")
            
            # 2. Try first RelatedTopic if Abstract is empty
            if text == "":
                topics = data.get("RelatedTopics", [])
                if topics and isinstance(topics[0], dict) and "Text" in topics[0]:
                    text = topics[0]["Text"]
            
            # 3. Try Heading as last resort
            if text == "":
                text = data.get("Heading", "")

            # 4. Final fallback
            if text == "":
                text = "Discovering the secrets of " + query

            return text

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_trivia = result
        return "Riddle Clue: " + result

    @gl.public.view
    def get_last_trivia(self) -> str:
        return self.last_trivia
