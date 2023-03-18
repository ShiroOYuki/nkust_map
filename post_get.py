import requests

response = requests.get("http://127.0.0.1:5000")
response.raise_for_status()
print(response.json())

obj = {"msg": "Hello, Server!"}
r = requests.post("http://127.0.0.1:5000/post", data=obj)
print(r.json())