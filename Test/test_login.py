# test the credentials.py file

from user import login, credentials
import json
import os


# test the login.py file
def test_login():
    # get the bearer token from tokens.json
    expected_token = None
    acc = credentials.Credentials
    lg = login.Login()
    with open('../user/tokens.json', 'r') as file:
        try:
            tokens = json.loads(file.read())
            if 'bearer_token' in tokens:
                expected_token = tokens['bearer_token']
        except json.decoder.JSONDecodeError:
            pass
    os.chdir('../Test/')
    actual_token = lg.login(acc[0], acc[1])
    assert expected_token is not None
    assert len(expected_token) > 0
    assert actual_token is not None
    assert len(actual_token) > 0
    assert len(expected_token) == len(actual_token)
    # clean up
    os.remove('../Test/tokens.json')