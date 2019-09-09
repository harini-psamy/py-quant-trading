from pylivetrader.api import order_target, record, symbol
import alpaca_trade_api as tradeapi

api = tradeapi.REST('PKP5E50T3Z70C9IZMTXO', 'VQfcGAQjji3U4kiSh0IxYTgfpAUs4i/YDO1Ik4ZV', api_version='v2') # or use ENV Vars shown below
account = api.get_account()
api.list_positions()

def initialize(context):
    
    context.sym = symbol(sym)
    context.account_bal = account-bal
    context.units = units
    
def handle_data(context, data):
    stock_data = data.history(context.asset, 'price', bar_count=100, frequency="1s")
       
    order_target(context.asset, units)
    
    record(MSFT=data.current(context.asset, 'price'), stock_data)


