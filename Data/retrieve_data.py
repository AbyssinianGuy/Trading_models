import requests
import json
import robin_stocks as rb

# open tokens.json and get the bearer token
class RetrieveData:
    input_path = '../user/tokens.json'
    output_path = '../Data/train_data.json'
    url = f"https://api.robinhood.com/marketdata/historicals/"
    with open(input_path, 'r') as f:
        tokens = json.load(f)
        bearer_token = tokens['bearer_token']

    # build the url
    def build_url(self, symbol: str, interval: str, span: str, bounds: str):
        url = f"https://api.robinhood.com/marketdata/historicals/"
        headers = {"Authorization": "Bearer "+self.bearer_token}
        filters = f"{symbol}/?interval={interval}&span={span}&bounds={bounds}"
        data = requests.get(url+filters, headers=headers)
        return data

    def get_historical_data(self, ticker: str, interval: str, span: str, bounds: str):
        response = self.build_url(ticker, interval, span, bounds)
        if response.status_code == 200:
            data = response.json()
            historical_data = data['historicals']
            for datapoint in historical_data:
                # save the json data to a file
                with open(self.output_path, 'w') as outfile:
                    json.dump(datapoint, outfile)
                return historical_data
        else:
            print("Error retrieving data", response.status_code)
            return None


if __name__ == "__main__":
    rd = RetrieveData()
    # open symbols.json and get the symbols
    instruments = rb.get_all_instruments()
    symbols = [instrument['symbol'] for instrument in instruments]
    print(symbols)
            # rd.get_historical_data(symbol, 'day', 'year', 'regular')