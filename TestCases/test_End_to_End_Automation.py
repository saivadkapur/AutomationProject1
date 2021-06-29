import requests
import json
import jsonpath

def test_AddStudentData():
    API_URL = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("D:\\AutomationSampleDataFiles\\RequestJson.json", "r")
    json_request = json.loads(file.read())
    response = requests.post(API_URL,json_request)
    #print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0]) #this id needs to be passed in tech request and address request post body and
    #as well as it has to be passed in final details get url

    TECH_URL = "http://www.thetestingworldapi.com/api/technicalskills"
    f1 = open('D:/AutomationSampleDataFiles/TechDetails.json', 'r')
    json_techReq = json.loads(f1.read())
    #Passing id & st_id values in the tech request body dynamically
    json_techReq['id'] = int (id[0])
    json_techReq['st_id'] = id[0]
    techResponse = requests.post(TECH_URL,json_techReq)
    print(techResponse.json())

    ADDRESS_URL = "http://www.thetestingworldapi.com/api/addresses"
    f2 = open('D:/AutomationSampleDataFiles/AddressDetails.json', 'r')
    json_addReq = json.loads(f2.read())
    json_addReq['stId'] = id[0]
    addResponse = requests.post(ADDRESS_URL,json_addReq)

    FINALDETAILS_URL = "http://www.thetestingworldapi.com/api/FinalStudentDetails/" + str (id[0])
    finalResponse = requests.get(FINALDETAILS_URL)
    print(finalResponse.text)

