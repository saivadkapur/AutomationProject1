import requests
import json
import jsonpath

#POST - Method
def test_AddStudentData():
    API_URL = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("D:\\AutomationSampleDataFiles\\RequestJson.json", "r")
    josn_request = json.loads(file.read())
    response = requests.post(API_URL,josn_request)
    #print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

#PUT - Method
def test_UpdateStudentData():
    API_URL = "http://www.thetestingworldapi.com/api/studentsDetails/328386"
    file = open("D:\\AutomationSampleDataFiles\\RequestJson.json", "r")
    josn_request = json.loads(file.read())
    response = requests.put(API_URL,josn_request)
    print(response.text)

#GET - Method
def test_GetStudentData():
    API_URL = "http://www.thetestingworldapi.com/api/studentsDetails/328386"
    response = requests.get(API_URL)
    #print(response.text)
    #parse the response body to json format this can be done in two ways
    #Way-1
    json_response = json.loads(response.text)
    #Way-2
    #json_response = response.json()

    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 328386
    print(json_response)

#DELTE - Method
def test_DeleteStudentData():
    API_URL = "http://www.thetestingworldapi.com/api/studentsDetails/328386"
    response = requests.delete(API_URL)
    print(response.text)

#Verify if the Student Data is been deleted or not
def test_GetStudentData():
    API_URL = "http://www.thetestingworldapi.com/api/studentsDetails/328386"
    response = requests.get(API_URL)
    print(response.text)
