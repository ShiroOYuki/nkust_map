from flask import Flask

app = Flask(__name__)

@app.route('/')
def listen():
    return {"msg": "Hello, World!"}

@app.route("/post")
def getdata(request):
    print(request.json())
    return {"msg": "Success!"}

if __name__ == '__main__':
    app.run()