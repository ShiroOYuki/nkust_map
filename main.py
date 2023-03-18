from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def listen():
    return {"msg": "Hello, World!"}

@app.route("/post", methods=["POST"])
def getdata():
    if request.method == "POST":
        datas = request.form
        print(datas["msg"])
        return {"msg": "Success!"}
    return {"msg": "Failed!"}

if __name__ == '__main__':
    app.run()