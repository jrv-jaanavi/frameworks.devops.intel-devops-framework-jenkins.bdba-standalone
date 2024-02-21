import subprocess
import sys
import os


scan_username = os.environ.get("ScanCred_USR")
scan_password = os.environ.get("ScanCred_PSW")

artifact_url = sys.argv[1]
download_artifact = f"curl -u {scan_username}:{scan_password} -O {artifact_url}"
subprocess.call(download_artifact, shell=True)

artifact_output = subprocess.run(['ls', '-l'], capture_output=True, text=True)

print(artifact_output.stdout)

pip_cmd = f"pip install --upgrade pip && pip install  abi==3.0.0 --extra-index-url=https://ubit-artifactory-or.intel.com/artifactory/api/pypi/one-windows-pypi-local/simple --proxy=http://proxy-chain.intel.com:912 "

pip_cmd_output = subprocess.run(pip_cmd, capture_output=True, text=True)

pkg_name = sys.argv[2]
bdba_scan_cmd = f"abi binary_scan scan --timeout 40 --wait --tool_url https://bdba001.icloud.intel.com --tool_group 6  --report_name BDBA_Report --include_components  --zip_file {pkg_name} --username {scan_username} --password {scan_password} --debug "
bdba_scan_cmd_output = subprocess.run(bdba_scan_cmd, capture_output=True, text=True)
