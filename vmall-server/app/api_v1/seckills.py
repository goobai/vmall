from . import bp
from flask import render_template, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import redis_client
import logging
from app.utils import *
from app.models import *
import ast


def limit_handler():
    # return: True: 允许; False: 拒绝
    amount_limit = 100  # 限制数量
    key_name = 'xxx_goods_limit'  # redis key name
    incr_amount = 1  # 每次增加数量
    # 判断key是否存在
    if not redis_client.exists(key_name):
        # setnx是原子性的，允许并发操作
        redis_client.setnx(key_name, 100)
    # 数据插入后再判断是否大于限制数
    if redis_client.incrby(key_name, incr_amount) <= amount_limit:
        return True
    return False


@bp.route('/good/seckill', methods=['GET', 'POST'])
def seckill():
    if limit_handler():
        print(1)
        logging.info("successful")
    else:
        print(2)
        logging.info("failed")
    return jsonify(data='''\//limit''')


@bp.route('/rdb')
def test():
    id = request.args.get('id')
    name = request.args.get('name')
    age = request.args.get('age')
    dic = {
        'age': age,
        'name': name,
        'id': id,
        'address': {
            "1": 1,
            "province": 13,
            "city": 3
        }
    }
    redis_client.hmset('user_info', dic)
    re = redis_client.hmget('user_info', 'name', 'age')
    all = redis_client.hgetall('user_info')
    print(all)
    return jsonify(data=all)


@bp.route('/gen/order/id')
def gen_order_id():
    order_id = generate_order_id(uid=1265634)
    return jsonify(orderId=order_id)


@bp.route('/test/appctx')
def app_cts():
    order_id = gen_id()
    res = current_app.id_pool
    return jsonify(res=res, order_id=order_id)


@bp.route('/test/1')
def cache_product():
    start = request.args.get('start')
    end = request.args.get('end')
    dic = {
        'age': 12,
        'name': 'goobai777',
        'id': 8888,
        'address': {
            "1": 1,
            "province": 13,
            "city": 3
        }
    }
    import time
    t0 = time.time()
    # cache1redis('key', bytes(str(dic), encoding='utf-8'))
    sku = ProductSku.query.filter_by(id=10).first()
    data = sku.to_dict()
    print(data)
    for x in range(int(start), int(end)):
        dic['id'] = x
        cache1redis(x, bytes(str(data), encoding='utf-8'))
    t2 = time.time() - t0

    return jsonify(code=1, body=t2)


@bp.route('/test/2')
def get_product():
    start = request.args.get('start')
    end = request.args.get('end')

    data = redis_client.get("order:amount")
    print(data)
    return jsonify(code=1, data=ast.literal_eval(data))


@bp.route('/imgs')
def modify_img():
    imgs = Img.query.filter_by(owner_type=3).all()
    for img in imgs:
        img.url = img.url.replace(r'/n5/jfs', r'/n1/jfs')
        img.url = img.url.replace(r'/n5/s54x54_jfs', r'/n1/s454x454_jfs')
        img.url = img.url.replace(r'/n5/s54x54', r'/n1/s454x454')
        img.url = img.url.replace(r'/n5/s50x64', r'/n1/s454x454')
        img.url = img.url.replace(r'/n5/s75x75', r'/n1/s454x454')
        img.url = img.url.replace(r'/n5/g15/', r'/n1/g15/')
    db.session.commit()
    return 'ok'


@bp.route('/db/trans')
def db_trans():
    cart = Cart(user_id=1, shop_id=1, count=1, checked=1)
    db.session.add(cart)
    cart_id = cart.id
    return jsonify(cart_id=cart_id)
