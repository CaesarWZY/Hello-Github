#enconding : utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style ='color:red'>Welcome to flask and hello world 你好啊</h1>"
    pass
if __name__ == '__main__':
    app.run(debug=True)
