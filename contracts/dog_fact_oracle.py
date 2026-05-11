# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class DogFactOracle(gl.Contract):
    """
    Chain Quest: Dog Breed Oracle
    Fetches REAL dog breed data from the Dog CEO API
    to generate companion pet attributes and lore text.
    Uses a deterministic breed endpoint for reliable consensus.
    """
    last_breed_info: str

    def __init__(self):
        self.last_breed_info = ""

    @gl.public.write
    def fetch_dog_breed(self, breed: str) -> str:
        if breed == "":
            breed = "labrador"

        url = "https://dog.ceo/api/breed/" + breed + "/images"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            status = data["status"]
            image_count = str(len(data["message"]))
            first_image = data["message"][0]
            return status + "|" + image_count + "|" + first_image

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_breed_info = breed + ": " + parts[1] + " images"
        return "Companion Pet: " + breed + " | Gallery: " + parts[1] + " images | Sample: " + parts[2]

    @gl.public.view
    def get_last_breed(self) -> str:
        return self.last_breed_info
