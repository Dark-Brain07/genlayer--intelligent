# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class NumberFactOracle(gl.Contract):
    """
    Chain Quest: Time & Lore Oracle
    Fetches REAL world time and timezone data from WorldTimeAPI
    to generate time-locked dungeon gates and events.
    Uses the simplest possible API for maximum consensus reliability.
    """
    last_time_info: str

    def __init__(self):
        self.last_time_info = ""

    @gl.public.write
    def fetch_world_time(self, timezone: str) -> str:
        if timezone == "":
            timezone = "Etc/UTC"

        # WorldTimeAPI (Very simple and reliable)
        url = "http://worldtimeapi.org/api/timezone/" + timezone

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            
            datetime = data.get("datetime", "")
            unixtime = str(data.get("unixtime", 0))
            return datetime + "|" + unixtime

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_time_info = result
        return "Time Synchronized: " + result

    @gl.public.view
    def get_last_time(self) -> str:
        return self.last_time_info
