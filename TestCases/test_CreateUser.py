import requests
import json
import jsonpath
import pytest

#API URL
url = "https://reqres.in/api/users"

def test_Create_User():
    #read input Json file
    file = open("D:\\AutomationSampleDataFiles\\CreateUser.json", "r")
    json_input = file.read()
    #Parse json_input string file to json object
    request_json = json.loads(json_input)

    #Now make post request along with the json body
    response = requests.get(url, request_json)

    #Validate the response code
    #print(response.status_code)
    assert response.status_code == 201

    #fetch header from response
    #print(response.headers)
    print(response.headers.get('Content-Type'))

    #Parse response to Json Format
    response_json = json.loads(response.text)
    print(response_json)

    #fetch the id from the response body
    data = jsonpath.jsonpath(response_json, 'data')
    print(data[0])
