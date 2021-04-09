from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return '<h1>Welcome to My Watchlist!</h1>'


@app.route('/hello/<name>')
def hello(name):
    return 'hello, %s' % name


@app.route('/to')
def dragon():
    return render_template('test.html')