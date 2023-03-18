from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def listen():
    if request.method == "POST":
        datas = request.form
        print(datas["msg"])
        return {"msg": "Success!"}
    elif request.method == "GET":
        return {"msg": "Hello, World!"}
    return {"msg": "Failed!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")