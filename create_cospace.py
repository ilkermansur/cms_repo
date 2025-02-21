import requests
import urllib3

# Güvenlik uyarılarını kapatma
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cisco Meeting Server bilgileri
cms_ip = '192.168.80.121'
username = "admin"
password = "cisco123"
name = 'python_test'
uri= 'python_uri'
callId= '12341234'
passcode = '4444'


payload = f'name={name}&uri={uri}&callId={callId}&passcode={passcode}'

url = f"https://{cms_ip}:445/api/v1/coSpaces"

# Headers

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.post(url, auth=(username, password), data=payload, headers=headers, verify=False)

print(response.status_code)
print(response.text)
