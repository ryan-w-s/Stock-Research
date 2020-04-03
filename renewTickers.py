import json
import urllib.request as request
from contextlib import closing

NASDAQ = "ftp://ftp.nasdaqtrader.com/symboldirectory/"
SOURCES = [
    NASDAQ + "nasdaqlisted.txt",
    NASDAQ + "otherlisted.txt"
]

def processStockFile(ftpUrl):
    stocks = dict()
    with closing(request.urlopen(ftpUrl)) as r:
      for line in r.readlines()[1:-1]:
          stocks.update(processStock(line))
    return stocks
          

def processStock(stockLine):
    ticker, name, *rest = stockLine.decode().split('|')
    return { ticker : name }

def writeJson(obj, path = "public/stocks.json"):
    with open(path, 'w') as f:
        json.dump(obj, f)

if __name__ == "__main__":
    stocks = dict()
    for source in SOURCES:
        stocks.update(processStockFile(source))
    writeJson(stocks)
    symbols = { "symbols": list(stocks.keys())}
    writeJson(symbols, "public/symbols.json")
