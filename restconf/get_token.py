```python
# Cisco DNA Center REST API
# Install requests:
# python3 -m pip install requests

import requests


# Cisco DNA Center URL
BASE_URL = "https://sandboxdnac2.cisco.com"


# Authentication details
credentials = {
    "username": "devnetuser",
    "password": "YOUR_PASSWORD"
}


# Disable SSL certificate warnings
# verify=False is used for the sandbox
requests.packages.urllib3.disable_warnings()


# Request an authentication token
def get_token():

    url = f"{BASE_URL}/dna/system/api/v1/auth/token"

    response = requests.post(
        url,
        auth=(credentials["username"], credentials["password"]),
        verify=False
    )

    # Check whether authentication was successful
    if response.status_code == 200:

        # Extract the token from the JSON response
        token = response.json()["Token"]

        return token

    else:
        print(f"Authentication failed: {response.status_code}")
        print(response.text)

        return None


# Request a token
token = get_token()


# Display the token if authentication was successful
if token:
    print(token)
```