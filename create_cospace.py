import requests
import urllib3

# Güvenlik uyarılarını kapatma
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cisco Meeting Server bilgileri
cms_ip = '192.168.80.121'
username = "admin"
password = "cisco123"

# coSpace Parametreleri
coSpace_data = {
    "name": "test_python",
    "uri": "test_python",
    "callId": "12341234",
    "passcode": "4444"
}

url = f"https://{cms_ip}:445/api/v1/coSpaces"

# Headers

headers = {'Content-Type': 'application/json'}

response = requests.post(url, auth=(username, password), json=coSpace_data, headers=headers, verify=False)

print(response.status_code)
print(response.text)
