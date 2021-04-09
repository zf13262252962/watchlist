from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
# 关闭对模型 修改的监控
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化扩展，传入程序实例 app
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


# name = 'D-wade'
# movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'}
# ]


# @app.route('/')
# @app.route('/home')
# def index():
#     return '<h1>Welcome to My Watchlist!</h1>'

# 模板上下文处理函数
@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


@app.route('/')
def index():
    # user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)


@app.route('/hello/<name>')
def hello(name):
    return 'hello, %s' % name


@app.route('/to')
def dragon():
    return render_template('test.html')


@app.route('/back/<int:year>')
def go_back(year):
    return 'welcome back to %s' % (2021 - year)


# @app.route('/like')
# def movie():
#     return render_template('index.html', name=name, movies=movies)

@app.errorhandler(404)
def page_404(e):
    # user = User.query.first()
    return render_template('404.html'), 404

