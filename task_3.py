import requests

title_name = input("input title: ")
body_text = input("input body text: ")


post_p = requests.post("https://jsonplaceholder.typicode.com/users/1/posts", 
                     params={'userId': 1}, data={'title': title_name, 'body': body_text} )
data = post_p.json()
print(data)