import requests

class ExchangeBase:
    def __init__(self, uri: str, path: str):
        """
        @param uri: The base URI of the exchange
        @param path: The path to the API
        
        """
        self.uri = uri
        self.path = path
        
    def __get_data(self, symbol: str) -> requests.Response:
        """
        Gets the data from the API and returns it as a JSON object
        @param path: The path to the API endpoint
        @return: The JSON object
        """
        return requests.get(self.uri + self.path + symbol).json()
    
    def get_price(self, symbol: str) -> requests.Response:
        return self.__get_data(symbol)
