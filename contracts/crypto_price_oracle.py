# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class CryptoPriceOracle(gl.Contract):
    """
    Chain Quest: Crypto Price Oracle
    Fetches REAL BTC price from Binance public API
    to set in-game gold exchange rates.
    """
    last_price: str

    def __init__(self):
        self.last_price = "0"

    @gl.public.write
    def fetch_btc_price(self) -> str:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.text)
            # Trim to integer for strict consensus
            price_int = str(int(float(data["price"])))
            return price_int

        btc_price = gl.eq_principle.strict_eq(_fetch)
        self.last_price = btc_price
        return "BTC Price: $" + btc_price

    @gl.public.view
    def get_price(self) -> str:
        return self.last_price
