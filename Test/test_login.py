# test the credentials.py file

import pytest
from user import login, credentials
import json

# test the login.py file
def test_login():
    # get the bearer token from tokens.json
    bearer_token = None
    acc = credentials.Credentials
    with open('tokens.json', 'r') as file:
        try:
            tokens = json.loads(file.read())
            if 'bearer_token' in tokens:
                bearer_token = tokens['bearer_token']
        except json.decoder.JSONDecodeError:
            pass
    # create an instance of login
    # assert login.login(acc[0], acc[1]) == bearer_token