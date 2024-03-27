import subprocess
import time
import sys
import os


scan_username = os.environ.get("ScanCred_USR")
scan_password = os.environ.get("ScanCred_PSW")

artifact_url = sys.argv[1]
download_artifact = f"curl -u {scan_username}:{scan_password} -O {artifact_url}"
download_artifact_split = download_artifact.split()
return_code = subprocess.run(download_artifact_split, capture_output=True, text=True)

print(return_code.stdout)
print(return_code.stderr)

print("BDBA execution")

pip_cmd1 = "pip install --upgrade pip"
pip_cmd_output1 = subprocess.run(pip_cmd, capture_output=True, text=True)
print(pip_cmd_output1.stdout)
print(pip_cmd_output1.stderr)

pip_cmd2 = "pip install abi==3.1.0 --extra-index-url=https://ubit-artifactory-or.intel.com/artifactory/api/pypi/one-windows-pypi-local/simple --proxy=http://proxy-chain.intel.com:912 "
pip_cmd_split2 = pip_cmd.split(",")
pip_cmd_output2 = subprocess.run(pip_cmd, capture_output=True, text=True)

print(pip_cmd_output2.stdout)
print(pip_cmd_output2.stderr)

timestamp = time.time()
pkg_name = sys.argv[2]
name, ext = os.path.splitext(pkg_name)
new_pkg_name = name + f"{timestamp}" + ext
os.rename(pkg_name,new_pkg_name)

return_code = subprocess.run(download_artifact_split, capture_output=True, text=True)

print(return_code.stdout)
print(return_code.stderr)

bdba_scan_cmd = f"abi binary_scan scan --timeout 40 --wait --tool_url https://bdba001.icloud.intel.com --tool_group 6  --report_name BDBA_Report --include_components  --zip_file {new_pkg_name} --username {scan_username} --password {scan_password} --debug "
bdba_scan_cmd_split = bdba_scan_cmd.split()
print("ABI Command :", bdba_scan_cmd_split)
bdba_scan_cmd_output = subprocess.run(bdba_scan_cmd_split, capture_output=True, text=True)

print(bdba_scan_cmd_output.stdout)
print(bdba_scan_cmd_output.stderr)
