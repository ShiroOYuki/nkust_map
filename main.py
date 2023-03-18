from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def listen():
    if request.method == "POST":
        datas = request.form
        print(datas)
        result = {"msg": "Success!", "password": "123", "id": "JACK", "status": "OK"}
        return result
    elif request.method == "GET":
        return {"msg": "Hello, World!"}
    return {"msg": "Failed!"}

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")

# post: {"msg": "Login", "ID": "C111151125", "pwd": "base_64_pwd"}
# response: {"msg": "Login", "status": "OK"}   200>0K   400>error  600>empty
# post: {"msg": "getNextClassInfo", "ID": "C111151125", "time": "1-1"}
# response: {"msg": "getNextClassInfo", "ID": "C111151125", "info": {"name": "class_name", "addr": "address"}, "status": "OK"}