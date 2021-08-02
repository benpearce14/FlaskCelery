from flask import Flask, render_template
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice
from datetime import datetime
from time import sleep

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_BACKEND'] = 'db+sqlite:///db.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

celery = make_celery(app)
db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    results = Results.query.order_by(Results.date_created).all()
    return render_template("index.html", results=results)


@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return "Async Request Sent"


@app.route('/insert_data', methods=["POST", "GET"])
def insert_data():
    insert.delay()
    return "Async Request to Insert Data Sent"


@app.route('/delete_all', methods=["POST", "GET"])
def delete_all():
    delete.delay()
    return "Async Request to Delete Data Sent"


@celery.task(name='app.reverse')
def reverse(string):
    sleep(5)
    return string[::-1]


@celery.task(name='app.insert')
def insert():
    sleep(10)
    for i in range(50):
        data = ''.join(choice('ABCDE') for i in range(10))
        result = Results(data=data)
        db.session.add(result)
    db.session.commit()
    return 'Data has been inserted'


@celery.task(name='app.delete')
def delete():
    sleep(10)
    db.session.query(Results).delete()
    db.session.commit()
    return 'Data has been deleted'


if __name__ == '__main__':
    app.run(debug=True)
