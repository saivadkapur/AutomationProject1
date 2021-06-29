import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get("https://github.com/login", auth=HTTPBasicAuth('sainath.vadkapur@gmail.com', 'Fazer@3412'))
    print(response.text)