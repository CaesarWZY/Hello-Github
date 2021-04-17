#enconding : utf-8
from flask import Flask, render_template, request, redirect, url_for, flash, session
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/',methods=['post','get'])
def index():
    content = request.form['content']
    print(content)
    return render_template('test.html')
@app.route('/')
#这边写search的功能
def search():
    pass

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=8003)
