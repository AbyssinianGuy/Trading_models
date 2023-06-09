from user import credentials
import json
import robinhood as rb
import os


# create a class that logs in to the Robinhood API and stores the bearer token
class Login:
    def __init__(self):
        # get the bearer token
        cr = credentials.Credentials
        self.bearer_token = None
        # check if tokens.json exists
        if os.path.exists('tokens.json'):
            with open('tokens.json', 'r') as file:
                try:
                    tokens = json.loads(file.read())
                    if 'bearer_token' in tokens:
                        self.bearer_token = tokens['bearer_token']
                except json.decoder.JSONDecodeError:
                    pass
        # set the headers

    def login(self, username: str, password: str):
        if self.bearer_token is not None:
            return self.bearer_token
        # login to Robinhood
        access_token = rb.login(username, password)
        # get the bearer token from access_token
        self.bearer_token = access_token


if __name__ == "__main__":
    l = Login()
    l.login('username', 'password')
    print(l.bearer_token)
