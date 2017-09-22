

import sys
import os
import time
#sys.path.insert(0,os.path.join(os.path.realpath(__file__),'..'))
#import my_dependencies; my_dependencies.check()
from rtstock.stock import Stock
import config
import threading

def stock_worker(sym):
    stock = Stock(sym)
    for i in range(100):
        try:
            data = stock.get_latest_price()[0]
            if data[u'LastTradeTime'] is None:
                print('Stock %s is unavailable. '%sym)
                break
            last_time = str(data[u'LastTradeTime'])
            price = float(str(data[u'LastTradePriceOnly']))
            print('{:<10}'.format(last_time+':') +  '{:<30}'.format('%0.2fUSD'%price))
        except:
            import traceback; traceback.print_exc()
            print('%s FAILED'%sym)
        time.sleep(10)



threads = []
for sym in config.symbols[:10]:
    t = threading.Thread(target=stock_worker, args=(sym,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
