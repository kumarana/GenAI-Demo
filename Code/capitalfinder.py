import requests

API_URL = "http://localhost:3100/api/v1/prediction/e36deb0c-84b8-4735-ad9e-3451ebc56392"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Argentina",
})

print(output)
