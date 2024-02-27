import json
import requests

BASE = "http://127.0.0.1:5000/users"

data = {"Username": "gedikli@gmail.com", "Password": "1564559"}

content_type = {
    "Content-Type": "application/json"
}

response = requests.post(BASE, data=json.dumps(data), headers=content_type)

print(response.json())