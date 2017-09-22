

import sys
import os
#sys.path.insert(0,os.path.join(os.path.realpath(__file__),'..'))
#import my_dependencies; my_dependencies.check()
from rtstock.stock import Stock
stock = Stock('AAPL')
while True:
    print(stock.get_latest_price())
