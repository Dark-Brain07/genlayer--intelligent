# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class EthGasOracle(gl.Contract):
    """
    Chain Quest: ETH Gas Oracle
    Fetches REAL ETH price from Binance to calculate
    in-game crafting costs dynamically.
    """
    last_eth_price: str

    def __init__(self):
        self.last_eth_price = "0"

    @gl.public.write
    def fetch_eth_price(self) -> str:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            price_int = str(int(float(data["price"])))
            return price_int

        eth_price = gl.eq_principle.strict_eq(_fetch)
        self.last_eth_price = eth_price
        return "ETH Price: $" + eth_price

    @gl.public.view
    def get_eth_price(self) -> str:
        return self.last_eth_price
