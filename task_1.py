import requests

params = {"limit": 5}

response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
if response.status_code == 200:
    data = response.json()
    print(f"{response.headers}\n\n\n\n")
    for i in range(5):
        
        print(data[i])

else:
    print("error")