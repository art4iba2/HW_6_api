import requests

city_name = input("input city name: ")

apii = ['06c30b68759a3c69234eaf479c0b6418']

response = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': city_name, 'units': 'metric', 'APPID': apii[0]})


data = response.json()
with open("test.txt", 'w') as f:
    for line in data:
        f.write(line)
f.close()
print("name", data['list'][0]['name'])
print("conditions:", data['list'][1]['weather'][0]['description'])
print("temp:", data['list'][1]['main']['temp'])
print("temp_min:", data['list'][1]['main']['temp_min'])
print("temp_max:", data['list'][1]['main']['temp_max'])
