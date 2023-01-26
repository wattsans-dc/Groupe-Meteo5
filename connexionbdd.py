import requests
import json

url = 'http://192.168.137.187:5000/humidity'
headers = {'Content-type': 'application/json'}
data = {'teaux_humidité': 50}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.text)

