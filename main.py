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
            encpwd = datas["pwd"]
            che = s.check(id, encpwd):
            if che == "True":
                result = {"msg": "Login", "status": "OK"}
            elif che == "incorrect":
                return {"msg": "Login", "status": "PWD_ERROR"}
            else:
                encpwd = datas["pwd"]
                user = newUser(id, encpwd)
                classes = user.getClass()
                if not classes:
                    return {"msg": "Login", "status": "FAILED"}
                s.add_user(id, encpwd)
                if s.add_class(classes):
                    
                    print("Success!")
                result = {"msg": "Login", "status": "OK"}
                return result
                
        if msg == "getNextClassInfo":
            s = sql()
            id = datas["ID"]
            t = datas["time"]
            next_class = s.get_single_class(id, t)
            if next_class:
                name = next_class["CName"]
                addr = next_class["CAddr"]
                result = {"msg": "getNextClassInfo", "name": name, "addr": addr, "room": addr[0], "status": "OK"}
            else:
                result = {"msg": "getNextClassInfo", "name": "", "addr": "", "room": "", "status": "EMPTY"}
        return result
    elif request.method == "GET":
        return {"msg": "Hello, World!"}
    return {"msg": "Failed!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

# post: {"msg": "Login", "ID": "C111151125", "pwd": "base_64_pwd"}
# response: {"msg": "Login", "status": "OK"}   200>0K   400>error  600>empty
# post: {"msg": "getNextClassInfo", "ID": "C111151125", "time": "1-1"}
# response: {"msg": "getNextClassInfo", "name": "class_name", "addr": "address", "status": "OK"}