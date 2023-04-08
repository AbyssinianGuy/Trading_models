import requests
import json

# open tokens.json and get the bearer token
class RetrieveData:
    input_path = '../tokens.json'
    output_path = '../Data/train_data.json'
    with open(input_path, 'r') as f:
        tokens = json.load(f)
        bearer_token = tokens['bearer_token']


    def get_historical_data(self, symbol: str, interval: str, span: str, bounds: str):
        url = f"https://api.robinhood.com/marketdata/historicals/{symbol}/?interval={interval}&span={span}&bounds={bounds}"
        headers = {"Authorization": "Bearer "+self.bearer_token}
        response = requests.get(url, headers=headers)
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
