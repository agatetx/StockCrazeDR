

import sys
import os
import json
#sys.path.insert(0,os.path.join(os.path.realpath(__file__),'..'))
#import my_dependencies; my_dependencies.check()
from googlefinance import getNews
from rtstock.stock import Stock
sym = 'AAPL'
stock = Stock(sym)
while True:
    print(stock.get_latest_price())
    print(json.dumps(getNews(sym), indent=2))
