#fetching certain data from the response of an request and passing that information into the other request body
#is called Request Chaining

import requests
import json
import jsonpath

def test_add_newStudent():
    global id
    add_url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("D:\\AutomationSampleDataFiles\\RequestJson.json", "r")
    json_addReq = json.loads(file.read())
    response = requests.post(add_url,json_addReq)
    json_addResponse = response.json()
    id = jsonpath.jsonpath(json_addResponse,'id')
    print(id[0])

def test_get_lastStudentDetails():
    get_url = "http://www.thetestingworldapi.com/api/studentsDetails/" + str (id[0])
    response = requests.get(get_url)
    print(response.text)
