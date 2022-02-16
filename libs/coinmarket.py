import json
from typing import List, TypedDict
from aiohttp import content_disposition_filename
import requests

CryptoCurrencyResponse = TypedDict('CryptoCurrency', 
{
    "name" : str,
    "symbol" : str,
    "slug": str,
    "is_active": int,
    "quote": TypedDict('Quote', {
        "price": float,
        "currency": str
        })
}
)

class CoinMarket:
    def __init__(self, api_key): # Start class passing CoinMarket API Key | Inicía a classe passando a chave da API CoinMarket 
        self.api_key = api_key
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        } # Headers for consuming API | Header para consumir API

class cryptoCurrency(CoinMarket): # Class that inherits CoinMarket Class Attributes | Classe que herda os Atributos da classe CoinMarket
    url = lambda self, symbol, convert : f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}&convert={convert}"
    def __init__(self, api_key): # Initiation of this class have same initiation of father Class | A inicialização dessa classe tem a mesma inicialização da classe Pai
        super().__init__(api_key)

    def info(self, symbol: str or tuple, convert: str = 'usd') -> list:
        """Return Crypto Currency Infos

        arguments:
        symbol -- Symbol of target cryptocurrency

        convert -- Currency of convertion
        Return: List of object that carry query currencies data
        """
        
        if type(symbol) == str:
            reformed_url = self.url(symbol, convert)
        elif type(symbol) == tuple:
            reformed_url = self.url(",".join(symbol), convert)
        
        result = json.loads(requests.get(reformed_url, headers=self.headers).text)
        result: dict = result['data']
        
        return [
            {
                "name" : result[key]['slug'],
                "symbol" : result[key]['symbol'],
                "slug": result[key]['slug'],
                "is_active": result[key]['is_active'],
                "quote": {
                    "price": result[key]['quote'][convert.upper()]['price'],
                    "currency": convert.upper()
                    }
            } for key in result.keys()
        ] # List comprehension with currency keys | List Comprehension com a chave das moedas 




