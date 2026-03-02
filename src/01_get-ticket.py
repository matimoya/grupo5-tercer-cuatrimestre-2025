import json
import requests
from constants import API_BASE_URL, API_USERNAME, API_PASSWORD

api_url = API_BASE_URL + "/ticket"

headers = {
    "content-type": "application/json"
}

body_json = {
    "username": API_USERNAME,
    "password": API_PASSWORD
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers)

print("Ticket request status: ", resp.status_code)
response_json = resp.json()
print (response_json)
serviceTicket = response_json["response"]["serviceTicket"]

print("The service ticket number is: ", serviceTicket)
