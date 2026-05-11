# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class XrpPriceOracle(gl.Contract):
    """
    Chain Quest: XRP Price Oracle
    Fetches REAL XRP/USDT price from Binance
    to calculate cross-realm travel costs.
    """
    last_xrp_price: str

    def __init__(self):
        self.last_xrp_price = "0"

    @gl.public.write
    def fetch_xrp_price(self) -> str:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = response.json()
            # Round to 2 decimal places for consensus stability
            price_str = str(round(float(data["price"]), 2))
            return price_str

        xrp_price = gl.eq_principle.strict_eq(_fetch)
        self.last_xrp_price = xrp_price
        return "XRP Price: $" + xrp_price

    @gl.public.view
    def get_xrp_price(self) -> str:
        return self.last_xrp_price
