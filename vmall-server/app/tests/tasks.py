from celery import Celery
import time

app = Celery('tasks', broker='amqp://goobai:Goobai!1@localhost:5672/goobai_vhost')


@app.task
def add(x, y):
    time.sleep(5)
    return x + y
