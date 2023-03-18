import requests

# http://112.105.57.117:5000/
response = requests.get("http://127.0.0.1:5000")
response.raise_for_status()
print(response.json())

# http://112.105.57.117:5000/
obj = {"msg": "Hello, Server!"}
r = requests.post("http://127.0.0.1:5000", data=obj) #123
print(r.json())