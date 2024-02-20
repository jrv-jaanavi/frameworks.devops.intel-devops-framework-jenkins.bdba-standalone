import requests
import sys

file_url = sys.argv[1]

post_url = "http://onekitscan.idoc.intel.com/api/v1/scan"

body = { "submitted_user": "jrv", "reference_id": "1234", "file_url": file_url }

post_response = requests.post(post_url, json=body)

post_response_json = post_response.json()

print("Response after uploading to BDBA server: ", post_response_json)

scan_id = post_response_json["id"]

get_url = f"http://onekitscan.idoc.intel.com/api/v1/scan?id={scan_id}"

get_response = requests.get(get_url)

get_response_json = get_response.json()

print("Status of scan: ", get_response_json)
