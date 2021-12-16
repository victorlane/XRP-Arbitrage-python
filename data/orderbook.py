import asyncio
import json
from websockets import connect
from .xrptypes import *

cmd = {
    "id": 4,
    "command": "book_offers",
    "taker_gets": {
        "currency": "XRP"
    },
    "taker_pays": {
        "currency": "534F4C4F00000000000000000000000000000000",
        "issuer": "rsoLo2S1kiGeCcn6hCUXVrCpGMWLrRrLZz"
    },
}

class Sologenic():

    def __init__(self):
        self.LAST_PRICE = self.__get_last_price()
        self.AVERAGE_PRICE = self.__get_average_price()

    async def __get_solo_offers(self, limit = 1):
        cmd["limit"] = limit
        async with connect("ws://s2.ripple.com:443/") as websocket:
            await websocket.send(json.dumps(cmd))
            data = json.loads(await websocket.recv())
            return Response.from_dict(data)

    def __convert_drops_to_xrp(self, drops):
        return float(drops) / 1000000

    def __get_last_price(self):
        r = asyncio.run(self.__get_solo_offers())
        response = r.to_dict()["result"]["offers"][0]
        return self.__convert_drops_to_xrp(response["TakerGets"]) / float(response["TakerPays"]["value"])

    def __get_average_price(self):
        r = asyncio.run(self.__get_solo_offers(limit=10))
        response = r.to_dict()["result"]["offers"]
        averages = [
            self.__convert_drops_to_xrp(offer["TakerGets"])
            / float(offer["TakerPays"]["value"])
            for offer in response
        ]

        return sum(averages) / len(averages)
    