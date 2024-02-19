import requests
import sys

file_url = sys.argv[1]

url = "http://onekitscan.idoc.intel.com/api/v1/scan"

body = { "submitted_user": "jrv", "reference_id": "1234", "file_url": file_url }

post_response = requests.post(url, json=body)

post_response_json = post_response.json()

print(post_response_json)
