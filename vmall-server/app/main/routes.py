from . import bp
from flask import render_template, current_app, jsonify, request
from app.celery_tasks import send_mail
import json
from app import db


@bp.route('/')
def index():
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from `user` where `id`=%s', args=('1'))
    data = cursor.fetchall()
    return render_template('index.html')


@bp.route('/main/index')
def main():
    return render_template('main/index.html')


@bp.route('/post', methods=["POST", "GET"])
def post():
    print(request.form)
    print(request.data)
    if request.method == 'POST':
        print(request.form.get('username'))
        return jsonify({
            "name": "goobai",
            "id": 1
        })
    else:
        return render_template('demo/ajax.html')


@bp.route('/send/mail', methods=['GET'])
def send_email():
    subject = "密码重置"
    recipients = ["834207470@qq.com"]
    body = "你好你重置密码的验证码是：956713"
    sender = current_app.config['MAIL_DEFAULT_SENDER']
    print(sender)
    ret = send_mail.delay(subject, sender, recipients, body)

    print(ret)
    return str(ret)


@bp.route('/item/')
def item():
    id = request.args.get('id', type=int)
    print(id)
    print(type(id))
    return render_template('main/item.html')


@bp.route('/swp/')
def swp():
    return render_template('main/swp.html')
