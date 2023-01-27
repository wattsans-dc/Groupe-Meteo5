import urequests as requests
import time

url = 'http://192.168.137.187:5000/data_from_sonde'

data = {'degre': moyenneTemp, 'teaux_humidite': moyenneHumid}
headers = {'content-type': 'application/json'}
response = requests.post(url, json=data, headers=headers)
