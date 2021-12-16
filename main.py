from data.exchanges import *
from data.orderbook import *
from flask import Flask, jsonify

# Find a better way to get the data rather than initializing the classes each time a function gets called, this is also very slow and inefficient.
def get_price_data():
    bitrue = Bitrue()
    bitforex = Bitforex()
    sologenic = Sologenic()
    return {
        "bitrue": {
            "SOLOUSDT": bitrue.SOLOUSDT,
            "XRPUSDT": bitrue.XRPUSDT,
        },
        "bitforex": {
            "SOLOUSDT": bitforex.SOLOUSDT,
            "XRPUSDT": bitforex.XRPUSDT,
        },
        "sologenic": {
            "LAST_PRICE": sologenic.LAST_PRICE,
            "AVERAGE_PRICE": sologenic.AVERAGE_PRICE,
            "SOLOUSDT": sologenic.LAST_PRICE * bitrue.XRPUSDT,   
        }
    }

app = Flask(__name__)

@app.route("/api/v2/arbitrage")
def arbitrage():
    return jsonify(get_price_data())
    
if __name__ == "__main__":
    app.run()