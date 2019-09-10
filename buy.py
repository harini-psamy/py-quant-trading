from pylivetrader.api import order_target, record, symbol
import alpaca_trade_api as tradeapi
import sys
import matplotlib.pyplot as plt
#hndl = tradeapi.REST()
api = tradeapi.REST(key_id = 'PKK3QYZDA5NDVLEV81S1', secret_key='LU8PBU9InDaoK1YD0MAlEHtXhTaQvPZVInr6Fifp',base_url='https://paper-api.alpaca.markets')#, api_version='v2') # or use ENV Vars shown below

account = api.get_account()
print("status: ",account.status)
print("positions:",api.list_positions())

api.cancel_all_orders()
Balance, symbol, units = sys.argv[1],sys.argv[2],sys.argv[3]

Balance = Balance.replace('--account_bal=','')
symbol = symbol.replace('--sym=','')
units = units.replace('--units=','')

api.submit_order(symbol = symbol, qty = units, side = 'buy', type = 'market', time_in_force ='gtc', limit_price=None, stop_price=None, client_order_id=None)


dates = matplotlib.dates.date2num(list_of_datetimes)
plt.plot(dates,account.portfolio_value)
#to add timestamp frequency
plt.show()
