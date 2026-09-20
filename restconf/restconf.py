```python
# RESTCONF
# Install Requests:
# python3 -m pip install requests

import json
import requests


# Disable SSL certificate warnings
# verify=False is used for the Cisco DevNet sandbox
requests.packages.urllib3.disable_warnings()


# Device connection details
BASE_URL = "https://devnetsandboxiosxe.cisco.com"

credentials = {
    "username": "admin",
    "password": "YOUR_PASSWORD"
}


# RESTCONF headers
# application/yang-data+json tells the device to return YANG data as JSON
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}


# RESTCONF endpoint for the IETF Interfaces YANG model
url = f"{BASE_URL}/restconf/data/ietf-interfaces:interfaces"


# Retrieve interface information
response = requests.get(
    url,
    auth=(credentials["username"], credentials["password"]),
    headers=headers,
    verify=False
)


# Check whether the request was successful
if response.status_code == 200:

    # Convert the JSON response into a Python dictionary
    interfaces = response.json()

    # Pretty-print the JSON response
    interfaces_show = json.dumps(interfaces, indent=2)
    print(interfaces_show)

else:
    print(response.status_code)


# RESTCONF endpoint for a specific interface
url = f"{BASE_URL}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"


# Configuration to send to the interface
data = {
    "description": "Changed by RESTCONF",
    "enabled": True
}


# Modify the interface using HTTP PATCH
response = requests.patch(
    url,
    auth=(credentials["username"], credentials["password"]),
    headers=headers,
    json=data,
    verify=False
)


# Check whether the configuration was successful
if response.status_code == 200:
    print("Interface configuration successful")

else:
    print(f"PATCH failed: {response.status_code}")
    print(response.text)
```