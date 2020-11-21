import robin_stocks
from collections import defaultdict

GROWTH = ['TSLA', 'PTON', 'FSLY', 'TTWO', 'ESTC']
VALUE = ['GE', 'FL', 'BGFV', 'SEN', 'DENN', 'CVS', 'INTC', 'JWN']

robin_stocks.login(username='raphael.deem@gmail.com', password='')
pos = robin_stocks.get_open_option_positions()
profile = robin_stocks.build_user_profile()
uncategorized = []
results = {'puts': 0 , 'growth': 0, 'value': 0}
total = 0

for p in pos:
    option_id =  p['option'].split('/')[-2]
    instrument = robin_stocks.get_option_instrument_data_by_id(option_id)
    ticker = instrument['chain_symbol']
    market = robin_stocks.get_option_market_data_by_id(option_id)
    if instrument['type'] == 'put':
        results['puts'] += round(float(market['mark_price']) * float(p['quantity']) * float(p['trade_value_multiplier'])/float(profile['equity']), 3)*100
    if ticker in GROWTH:
        results['growth'][instrument['type']] += round(float(market['mark_price']) * float(p['quantity']) * float(p['trade_value_multiplier'])/float(profile['equity']), 3)*100
    elif ticker in VALUE:
        results['value'][instrument['type']] += round(float(market['mark_price']) * float(p['quantity']) * float(p['trade_value_multiplier'])/float(profile['equity']), 3)*100
    else:
        uncategorized.append(ticker)
        results['na'][instrument['type']] += round(float(market['mark_price']) * float(p['quantity']) * float(p['trade_value_multiplier'])/float(profile['equity']), 3)*100
    total += float(market['mark_price']) * float(p['quantity']) * float(p['trade_value_multiplier'])


import pdb; pdb.set_trace()
print(uncategorized)
print(results)
