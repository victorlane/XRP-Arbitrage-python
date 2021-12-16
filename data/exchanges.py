from .base import *
from dataclasses import dataclass

class Bitrue(ExchangeBase):

    def __init__(self):
        super().__init__("https://openapi.bitrue.com", "/api/v1/ticker/price?symbol=")

        self.SOLOUSDT = float(self.get_price("SOLOUSDT")["price"])
        self.XRPUSDT = float(self.get_price("XRPUSDT")["price"])


class Bitforex(ExchangeBase):

    def __init__(self):
        super().__init__("https://api.bitforex.com", "/api/v1/market/ticker?symbol=")

        self.SOLOUSDT = float(self.get_price("coin-usdt-solo")["data"]["buy"])
        self.XRPUSDT = float(self.get_price("coin-usdt-xrp")["data"]["buy"])
