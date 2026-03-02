import json
import os
import requests
from dotenv import load_dotenv
from constants import API_BASE_URL

load_dotenv()

api_url = API_BASE_URL + "/network-device"

headers={"X-Auth-Token": os.getenv("AUTH_TOKEN")}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print(json.dumps(response_json, indent=4))
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
