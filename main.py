from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def listen():
    if request.method == "POST":
        datas = request.form
        print(datas["msg"])
        result = {"msg": "Success!", "password": "123", "id": "JACK", "status": "OK"}
        return result
    elif request.method == "GET":
        return {"msg": "Hello, World!"}
    return {"msg": "Failed!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")