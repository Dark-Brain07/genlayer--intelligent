# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class WeatherBattleOracle(gl.Contract):
    """
    Chain Quest: Weather Battle Oracle
    Fetches REAL weather data from Open-Meteo API to determine
    battle conditions (fire/ice/storm modifiers).
    """
    last_temperature: str
    last_condition: str

    def __init__(self):
        self.last_temperature = ""
        self.last_condition = "unknown"

    @gl.public.write
    def fetch_battle_weather(self, lat: str, lon: str) -> str:
        url = "https://api.open-meteo.com/v1/forecast?latitude=" + lat + "&longitude=" + lon + "&current_weather=true"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response)
            temp = str(data["current_weather"]["temperature"])
            return temp

        temperature = gl.eq_principle.strict_eq(_fetch)
        self.last_temperature = temperature

        temp_val = int(float(temperature))
        if temp_val > 35:
            self.last_condition = "FIRE"
        elif temp_val < 5:
            self.last_condition = "ICE"
        else:
            self.last_condition = "NEUTRAL"

        return "Temperature: " + temperature + "C | Battle Condition: " + self.last_condition

    @gl.public.view
    def get_condition(self) -> str:
        return self.last_condition
