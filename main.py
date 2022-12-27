import requests
import pickle
import json

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

# print(f"url = {URL}\n\nheaders = {HEADERS}\n\ndata = {body}")

resp = requests.request(
    "POST", url=URL, headers=HEADERS, json=body,
)

#cache the response to keep working with data and not pay for API yet
with open("cache/prop_resp_intl.txt", "wb") as f:
    pickle.dump(resp,f)

with open("cache/prop_resp_intl.txt", "rb") as f:
    f_resp = pickle.load(f)

print(f_resp.json())