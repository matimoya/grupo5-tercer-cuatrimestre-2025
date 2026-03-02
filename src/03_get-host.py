import json
import os
import requests
from dotenv import load_dotenv
from constants import API_BASE_URL

load_dotenv()

api_url = API_BASE_URL + "/host"

headers={"X-Auth-Token": os.getenv("AUTH_TOKEN")}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
print(json.dumps(response_json, indent=4))
print()
hosts = response_json["response"]

for host in hosts:
    print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])
