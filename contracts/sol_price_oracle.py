# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class SolPriceOracle(gl.Contract):
    """
    Chain Quest: SOL Price Oracle
    Fetches REAL SOL/USDT price from Binance
    to set potion and spell costs in the game.
    """
    last_sol_price: str

    def __init__(self):
        self.last_sol_price = "0"

    @gl.public.write
    def fetch_sol_price(self) -> str:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response)
            price_int = str(int(float(data["price"])))
            return price_int

        sol_price = gl.eq_principle.strict_eq(_fetch)
        self.last_sol_price = sol_price
        return "SOL Price: $" + sol_price

    @gl.public.view
    def get_sol_price(self) -> str:
        return self.last_sol_price
