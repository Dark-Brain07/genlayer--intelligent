# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class BnbPriceOracle(gl.Contract):
    """
    Chain Quest: BNB Price Oracle
    Fetches REAL BNB/USDT price from Binance
    to determine guild treasury value.
    """
    last_bnb_price: str

    def __init__(self):
        self.last_bnb_price = "0"

    @gl.public.write
    def fetch_bnb_price(self) -> str:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = response.json()
            price_int = str(int(float(data["price"])))
            return price_int

        bnb_price = gl.eq_principle.strict_eq(_fetch)
        self.last_bnb_price = bnb_price
        return "BNB Price: $" + bnb_price

    @gl.public.view
    def get_bnb_price(self) -> str:
        return self.last_bnb_price
