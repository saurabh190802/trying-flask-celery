from flask import Flask
from flask_celery import make_celery
from celery.schedules import crontab
app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = "redis://localhost:6379/0"
app.config['CELERY_BACKEND'] = "redis://localhost:6379/0"
app.config['timezone'] = 'Asia/Kolkata'
app.config['beat_schedule'] = {
    'say-every-5-seconds': {
        'task': 'test',
        'schedule': crontab(hour=22, minute=46, day_of_week=3)
    },
}

celery = make_celery(app)


@celery.task(name='test')
def test():
    print("hello")
    return "hello"


@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    print("hello")
    return "sent async"


@celery.task(name=' celery_example.reverse')
def reverse(string):
    return string[::-1]


if __name__ == '_main_':
    app.run(debug=True)
