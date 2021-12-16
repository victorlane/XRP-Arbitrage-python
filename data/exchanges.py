from .base import *


class Bitrue(ExchangeBase):

    def __init__(self):
        super().__init__("https://openapi.bitrue.com", "/api/v1/ticker/price?symbol=")

        self.SOLOUSDT = self.get_price("SOLOUSDT")["price"]
        self.XRPUSDT = self.get_price("XRPUSDT")["price"]


bitrue = Bitrue()


class Bitforex(ExchangeBase):

    def __init__(self):
        super().__init__("https://api.bitforex.com", "/api/v1/market/ticker?symbol=")

        self.SOLOUSDT = self.get_price("coin-usdt-solo")["data"]["buy"]
        self.XRPUSDT = self.get_price("coin-usdt-xrp")["data"]["buy"]


bitforex = Bitforex()
