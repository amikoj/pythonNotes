from flask import url_for,Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/getUserById')
def getUser(id):
    return f'当前用户Id:{id}'

@app.route('/user/<username>')
def user(username):
    return f'访问者：{username}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'子路径 {escape(subpath)}'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('getUser',id=1000))
    print(url_for('user',username="蔡海飞"))
    print(url_for('show_subpath', subpath='subpath/b'))