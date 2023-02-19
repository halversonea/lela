import json
import requests

from auth import *

HEADERS = {
    'Authorization': "Bearer " + BEARER,
    'Content-Type': 'application/json',
}

URL = "https://api.datafiniti.co/v4/properties/search"

body = {
  "query": "-country:US AND propertyType:\"Single Family Dwelling\"",
  "num_records": 10,
}

resp = requests.request(
    "POST", url=URL, headers=HEADERS, json=body,
)

print(resp.json())