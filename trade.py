import robinhood
from user import credentials
from Data import retrieve_data

# Login to Robinhood
robinhood.login(credentials.username, credentials.password)

# Get the current price of a stock
symbol = 'AAPL'
interval = 'day'
span = 'year'
bounds = 'regular'

if '__main__' == __name__:
    retrieve_data.get_historical_data(symbol, interval, span, bounds)