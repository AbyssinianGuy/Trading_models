import requests
import json

# open tokens.json and get the bearer token
with open('tokens.json', 'r') as f:
    tokens = json.load(f)
    bearer_token = tokens['bearer_token']


def get_historical_data(symbol: str, interval: str, span: str, bounds: str):
    url = f"https://api.robinhood.com/marketdata/historicals/{symbol}/?interval={interval}&span={span}&bounds={bounds}"
    headers = {"Authorization": "Bearer "+bearer_token}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        historical_data = data['historicals']
        for datapoint in historical_data:
            # save the json data to a file
            with open('Data/train_data.json', 'w') as outfile:
                json.dump(datapoint, outfile)
            print(datapoint['begins_at'], datapoint['close_price'])
    else:
        print("Error retrieving data", response.status_code)
