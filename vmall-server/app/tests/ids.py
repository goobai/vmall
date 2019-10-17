from flask import Flask, request, jsonify, render_template
from redis import Redis
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer)
    title = db.Column(db.String(140))
    content = db.Column(db.Text())
    publish_time = db.Column(db.DateTime, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, default=datetime.utcnow)
    like = db.Column(db.Integer, default=0)
    dislike = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Article {}>'.format(self.content)


@app.route('/')
def index():
    db.create_all()
    article = Article(author_id=1, title="my test sql", content='''from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username''')
    db.session.add(article)
    db.session.commit()
    return jsonify(id=article.id)


@app.route('/fread')
def home():
    lines = ''
    with open('./dict.txt', mode='r', encoding='utf-8') as f:
        lines = f.read()

    return lines


@app.route('/query/<id>')
def query(id):
    article = Article.query.filter_by(id=id).first()

    if article:
        return jsonify(id=article.id)
    else:
        return jsonify(msg="not founded")


@app.route('/insert')
def insert():
    article = Article(title="you are loser", content="i cant agree", like=1)
    db.session.add(article)
    db.session.commit()
    res = db.session.execute("select * from article where id<10")
    for re in res:
        print(re)
    return jsonify(msg="suc")


if __name__ == '__main__':
    app.run(debug=True)
