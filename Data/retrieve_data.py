import requests
from user.credentials import Credentials
import json
import robin_stocks as rb


# open tokens.json and get the bearer token
def login(username: str, password: str):
    rb.robinhood.login(username, password)
    return rb


class RetrieveData:
    output_path = '../Data/train_data.json'
    input_path = '../user/tokens.json'
    url = 'https://api.robinhood.com/instruments/'
    bearer_token = None
    r = rb.robinhood
    c = Credentials

    def __init__(self):
        with open(self.input_path, 'r') as f:
            tokens = json.load(f)
            self.bearer_token = tokens['bearer_token']
            self.r.login(username=self.c[0], password=self.c[1])

    def get_data(self, symbol: str, interval: str, span: str):
        """
        Get data from Robinhood API
        :param symbol:  The symbol of the stock
        :param interval:  The interval of the data (5minute, 10minute, hour, day, week)
        :param span:  The span of the data (day, week, month, 3month, year, 5year, all)
        :return:  None
        """
        # with open (self.output_path, 'w') as outfile:
        #     json.dump(self.r.stocks.get_stock_historicals(symbol, interval=interval, span=span), outfile)
        try:
            data = self.r.stocks.get_stock_historicals(symbol, interval=interval, span=span)
        except requests.exceptions.HTTPError:
            data = None
        return data

    def save_data(self, data: dict):
        """
        Save the data to a json file
        :return:  None
        """
        with open(self.output_path, 'w') as outfile:
            json.dump(data, outfile)
        print('Data saved to {}'.format(self.output_path))
        return None

    def get_all_symbols(self):
        """
        Get all symbols from Robinhood API
        :return: None
        """
        all_instruments = {"tradeable": [], "non-tradeable": []}
        instruments_data = rb.robinhood.helper.request_get(self.url, 'pagination')
        all_instruments['tradeable'] = [i['symbol'] for i in instruments_data if i['tradeable']]
        all_instruments['non-tradeable'] = [i['symbol'] for i in instruments_data if not i['tradeable']]

        # save all_instruments to a json file
        with open('../Data/symbols.json', 'w') as outfile:
            json.dump(all_instruments, outfile)
        self.r.logout()
        return None


if __name__ == "__main__":
    rd = RetrieveData()
    with open('symbols.json', 'r') as f:
        symbols = json.load(f)

    five_year_data = {}
    for s in symbols['tradeable'] or symbols['non-tradeable']:
        res = rd.get_data(s, 'day', '5year')
        print(s, end='\n')
        if res is not None:
            five_year_data[s] = rd.get_data(s, 'day', '5year')
    rd.save_data(five_year_data)
