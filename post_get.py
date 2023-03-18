import requests

# http://112.105.57.117:5000/
response = requests.get("http://127.0.0.1:5000")
response.raise_for_status()
print(response.json())

# http://112.105.57.117:5000/
# obj = {"msg": "Login", "ID": "C111151115", "pwd": "QmFieTA1MTg="}
obj = {"msg": "Login", "ID": "C111151125", "pwd": "YWFhNzA4NTU="}
r = requests.post("http://127.0.0.1:5000", data=obj) #123
print(r.json())

obj = {"msg": "getNextClassInfo", "ID": "C111151125", "time": "2-8"}
r = requests.post("http://127.0.0.1:5000", data=obj) #123
print(r.json())