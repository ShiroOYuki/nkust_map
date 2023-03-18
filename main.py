from flask import Flask, request
from nkust_map.process import sql, newUser
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def listen():
    if request.method == "POST":
        datas = request.form
        print(datas)
        msg = datas["msg"]
        if msg == "Login":
            s = sql()
            id = datas["ID"]
            if s.check(id):
                result = {"msg": "Login", "status": "Exist"}
            else:
                encpwd = datas["pwd"]
                user = newUser(id, encpwd)
                if s.add_user(id, encpwd):
                    classes = user.getClass()
                    if s.add_class(classes):
                        print("Success!")
                result = {"msg": "Login", "status": "OK"}
                
        if msg == "getNextClassInfo":
            s = sql()
            id = datas["ID"]
            t = datas["time"]
            next_class = s.get_single_class(id, t)
            name = next_class["CName"]
            addr = next_class["CAddr"]
            result = {"msg": "getNextClassInfo", "name": name, "addr": addr, "status": "OK"}
        return result
    elif request.method == "GET":
        return {"msg": "Hello, World!"}
    return {"msg": "Failed!"}

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")

# post: {"msg": "Login", "ID": "C111151125", "pwd": "base_64_pwd"}
# response: {"msg": "Login", "status": "OK"}   200>0K   400>error  600>empty
# post: {"msg": "getNextClassInfo", "ID": "C111151125", "time": "1-1"}
# response: {"msg": "getNextClassInfo", "name": "class_name", "addr": "address", "status": "OK"}