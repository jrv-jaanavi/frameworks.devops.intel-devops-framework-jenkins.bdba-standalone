import requests
import datetime
import time
import os

token_gen_url = "https://onekitapi.intel.com/api/v1/auth/azure_token_generation"
file_status_fetch = "https://onekitapi.intel.com/api/v1/Package/Files/818930"
forced_sec_scan = "https://onekitapi.intel.com/api/v1/securityscans/scan"

scan_username = os.environ.get("Authtoken_USR")
scan_password = os.environ.get("Authtoken_PSW")

token_response = requests.post(token_gen_url, auth=(scan_username, scan_password), verify=False).json()
print("response from post:", token_response)
temp_token = token_response['data']['access_token']
print("print token:", temp_token)

headers = {"X-access": temp_token, "accept": "application/json", "Content-Type": "application/json"}
body = {"type": "file", "id": "19cdb721-fbcb-4006-9bbb-08b765565600", "forced": True}
upload_time = datetime.datetime.utcnow()
scan_response = requests.post(forced_sec_scan, json=body, headers=headers, verify=False)

print("response from post", scan_response.json())

iterations = 5000
for i in range(iterations):
    headers_status_fetch = {"X-access": temp_token, "accept": "application/json", "Content-Type": "application/json"}
    status_fetch_response = requests.get(file_status_fetch, headers=headers_status_fetch, verify=False)
    scan_response_json = status_fetch_response.json()
    scan_result = scan_response_json[0]["scanResult"]
    print("Scan status :", scan_result)
    if scan_result == "non-compliant" or scan_result == "compliant":
        break
    time.sleep(120)
    iterations -= 1
    if i == iterations - 1:
        print("Retry exceeded")
        break

scan_complete_time = datetime.datetime.utcnow()
time_taken = (scan_complete_time - upload_time).total_seconds()

print("Time taken for the scan:", time_taken)




