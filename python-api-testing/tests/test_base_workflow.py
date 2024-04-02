# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://api.trello.com/1/cards"

headers = {
  "Accept": "application/json"
}

id_list = '5abbe4b7ddc1b351ef961414'
api_key = 'APIKey'
api_token = 'APIToken'
query = {
  'idList': id_list,
  'key': api_key,
  'token': api_token
}

response = requests.request(
   "POST",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))