import requests
import json
import jsonpath

def test_oauth_authorization():
    "In order to access the OAUTH API URL you first have to generate the TOKEN and use that TOKEN to Access It"
    OAUTH_URL = "http://thetestingworldapi.com/Token"
    data = {'grant_type':'password', 'username':'admin', 'password':'password'}
    response = requests.post(OAUTH_URL,data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization': 'Bearer '+token_value[0]}
    API_URL = "http://www.thetestingworldapi.com/api/StDetails/328420"
    response = requests.get(API_URL, headers=auth)
    print(response.text)
