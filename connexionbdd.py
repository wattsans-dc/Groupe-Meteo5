import requests

url = 'http://192.168.137.187:5000/data_from_sonde'
data = {'degré': 69, 'teaux_humidité': 420}
headers = {'Content-type': 'application/json'}
response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.text)
