from . import bp
from flask import jsonify, request, redirect, url_for
from app.models import *
from flask_jwt_extended import jwt_required, create_refresh_token, create_access_token, get_jwt_identity
from sqlalchemy import desc, or_, and_
import datetime
from sqlalchemy import func


def home():
    pass


@bp.route('/<shopname>/card')
def shop_card(shopname):
    db


@bp.route('/chat/send', methods=["POST"])
@jwt_required
def send_message():
    receiver = request.json.get("receiver")
    body = request.json.get("body")

    if isinstance(receiver, int) and isinstance(body, str):
        sender_id = get_jwt_identity()
        message = Message(sender_id=sender_id, receiver_id=receiver, body=body)
        db.session.add(message)
        db.session.commit()
        return jsonify(code=1, message="发送成功！")
    else:
        return jsonify(code=0, message="参数错误！")


@bp.route('/chat/receive', methods=["POST"])
@jwt_required
def received_message():
    uid = get_jwt_identity()
    receiver = request.json.get('receiver')
    offset = request.json.get('offset')
    if isinstance(receiver, int):
        messages = Message.query.filter(
            or_(and_(Message.receiver_id == uid, Message.sender_id == receiver, Message.status == 0),
                and_(Message.sender_id == uid, Message.receiver_id == receiver, Message.status == 0))).offset(
            offset).all()
        if messages:

            data = [message.to_dict() for message in messages]
            return jsonify(code=1, data=data, message="查询成功！")
        else:
            return jsonify(code=1, data="", message="暂无新消息！")
    else:
        return jsonify(code=0, data="", message="参数错误！")
