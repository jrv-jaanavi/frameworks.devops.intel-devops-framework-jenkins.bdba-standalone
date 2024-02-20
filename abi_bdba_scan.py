import subprocess
import sys
import os


scan_username = os.environ.get("ScanCred_USR")
scan_password = os.environ.get("ScanCred_PSW")

artifact_url = sys.argv[1]
download_artifact = f"curl -u {scan_username}:{scan_password} -O {artifact_url}"
subprocess.call(download_artifact, shell=True)

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

print(result.stdout)
