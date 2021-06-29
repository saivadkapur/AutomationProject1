import requests
import json
import jsonpath
import openpyxl
from DataDrivenFramework import library

def test_add_multiple_students():
    #API
    add_url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open('D:/AutomationSampleDataFiles/RequestJson.json', 'r')
    json_request = json.loads(file.read())
    excelPath = 'D:/AutomationSampleDataFiles/StudentsMultipleData.xlsx'
    obj = library.Common(excelPath, 'Sheet1')
    rows = obj.fetch_noof_rows()
    columns = obj.fetch_noof_columns()
    keyList = obj.fetch_keyname_jsonreqbody()

    for i in range(2,rows+1):
        updated_json_request_body = obj.update_requestbodywith_data(i,json_request,keyList)
        response = requests.post(add_url,updated_json_request_body)
        print(response.text)








