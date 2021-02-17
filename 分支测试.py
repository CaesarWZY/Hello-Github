from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style ='color:blue'>现在是分支测试</h1>"
    pass
if __name__ == '__main__':
    app.run(debug=True)
