import requests

title_name = input("input title: ")
body_text = input("input body text: ")

post_p = requests.post("https://jsonplaceholder.typicode.com/users/1/posts", 
                       params={'userId': 1}, 
                       data={'title': title_name, 'body': body_text})

if post_p.status_code == 201:
    data = post_p.json()
    print(data)
elif post_p.status_code == 400:
    print("Bad Request: invalid input data")
elif post_p.status_code == 404:
    print("Not Found: the requested resource does not exist")
elif post_p.status_code == 500:
    print("Server Error: try again later")
else:
    print(f"Unexpected error: {post_p.status_code}")
