import sys
sys.path.append('../')
from libs.coinmarket import *
from libs.coinmarket import CryptoCurrencyResponse
from time import sleep
# 333 requisições por dia
# Ideal: 1 requisição a cada 5 minutos
crypto = cryptoCurrency('88868a7e-4960-4171-9c20-022b380eb6b3')
result: List[CryptoCurrencyResponse] = crypto.info('lus', 'brl')
for currency in result:
    print(f"Currency: {currency['name']} | Valor: R${currency['quote']['price']:.2f}")