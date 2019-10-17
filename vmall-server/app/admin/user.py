from . import bp
from flask import jsonify, request, redirect, url_for
from app.models import *
from flask_jwt_extended import jwt_required, create_refresh_token, create_access_token, get_jwt_identity
import datetime
from sqlalchemy import or_


@bp.route('/')
def index():
    pass


@bp.route('/user/reg', methods=['POST'])
def register():
    """
    用户注册
    :return:
    """
    if request.method == 'POST':
        username = request.json.get('username')
        email = request.json.get('email')
        phone = request.json.get('phone')
        password = request.json.get('password')
        user = User.query.filter(or_(User.username == username, User.phone == phone, User.email == email)).first()
        if not user:
            user = User(username=username, email=email, phone=phone)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'code': 1, 'data': user.to_dict(), 'message': '注册成功！'})
        else:
            return jsonify({'code': 0, 'data': {'username': user.username}, "msg": "该用户已经存在！"})
    else:
        return jsonify({'code': 0, 'data': {}, "msg": "请求错误，不支持该方法"})


@bp.route('/user/login', methods=['POST'])
def login():
    """
    用户登陆
    :return:
    """
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        if not username:
            return jsonify({"msg": "Missing username in request body"}), 0
        if not password:
            return jsonify({"msg": "Missing password in request body"}), 0
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id, user_claims=user.to_dict(),
                                               expires_delta=datetime.timedelta(hours=9))
            refresh_token = create_refresh_token(identity=user.id, expires_delta=datetime.timedelta(days=15))
            return jsonify(
                {'code': 1, 'data': {'access_token': access_token, 'refresh_token': refresh_token,
                                     'user_info': user.to_dict()}, 'message': '登陆成功！'}

            )
        else:
            return jsonify({'code': 0, 'data': {}, "msg": "Bad username or password"})


# 修改密码
@bp.route('/user/<username>/changepwd', methods=['POST'])
@jwt_required
def change_pwd(username):
    """
    修改密码
    :param username:
    :return:
    """
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        new_pwd = request.json.get('new_password')
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 0
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 0
        if not new_pwd:
            return jsonify({"msg": "Missing new password parameter"}), 0
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            user.set_password(new_pwd)
            db.session.commit()
            return jsonify(
                {'code': 1, 'data': {}, 'message': '密码修改成功！'}

            )
        else:
            return jsonify({'code': 0, 'data': {}, "msg": "Bad username or password"})


@bp.route('/user/card', methods=['GET'])
def user_card():
    uid = request.args.get('uid')
    print(uid)
    data = User.get_profile(uid)
    print(data)
    if data:
        return jsonify({'code': 1, 'data': data, 'message': '查询成功！'})
    else:
        return jsonify({'code': 0, 'data': data, 'message': '查询失败！'})


@bp.route('/user/info')
def user():
    username = request.args.get('username')
    info = User.get_profile(username=username)
    return jsonify()


@bp.route('/user/address', methods=['GET', 'POST'])
@jwt_required
def address():
    user_id = get_jwt_identity()
    if request.method == "GET":
        addrId = request.args.get('id')
        if addrId:
            data = UserAddress.query.filter_by(user_id=user_id, id=addrId).first()
            if data:
                return jsonify({'code': 1, 'data': data.to_dict(), 'message': '查询成功！'})
            else:
                return jsonify({'code': 0, 'data': {}, 'message': '无地址！'})
        else:
            data = UserAddress.query.filter_by(user_id=user_id, isDefault=1).first()
            if data:
                return jsonify({'code': 1, 'data': data.to_dict(), 'message': '查询成功！'})
            else:
                return jsonify({'code': 0, 'data': {}, 'message': '无地址！'})
    if request.method == "POST":
        data = request.json
        opType = request.json.get('type')  # 操作type：1：添加， 2：修改，3：删除
        if opType == 1:
            addr = UserAddress(user_id=data.get('userId'), address_detail=data.get('addressDetail'),
                               area_code=data.get('areaCode'), city=data['city'], county=data['county'],
                               isDefault=data['isDefault'], name=data.get('name'), postal_code=data.get('postalCode'),
                               province=data.get('province'), phone=data.get('tel'))
            db.session.add(addr)
            db.session.commit()
            return jsonify(code=1, data="添加成功！", msg="添加成功")
        elif opType == 2:
            address_id = request.json.get('id')
            addr = UserAddress.query.filter_by(user_id=user_id, id=address_id).first()
            if addr:
                addr.user_id = data['userId']
                addr.address_detail = data['addressDetail']
                addr.area_code = data['areaCode']
                addr.city = data['city']
                addr.county = data['county']
                addr.isDefault = data['isDefault']
                addr.name = data['name']
                addr.postal_code = data['postalCode']
                addr.province = data['province']
                addr.phone = data['tel']
                db.session.commit()
                return jsonify(code=1, data="修改成功！", msg="修改成功")
            else:
                return jsonify(code=0, data="此用户地址不存在！", msg="修改失败")
        elif opType == 3:
            address_id = request.json.get('id')
            addr = UserAddress.query.filter_by(user_id=user_id, id=address_id).first()
            if addr:
                db.session.delete(addr)
                db.session.commit()
                return jsonify(code=1, data="删除成功！", msg="删除成功！")
            else:
                return jsonify(code=0, data="此用户地址不存在！", msg="删除失败")
        else:
            return jsonify(code=0, msg="不支持当前操作！")


@bp.route('/user/addresses', methods=['GET', 'POST', 'PUT'])
@jwt_required
def addresses():
    if request.method == "GET":
        user_id = get_jwt_identity()
        data = UserAddress.query.filter_by(user_id=user_id).all()
        if data:
            return jsonify({'code': 1, 'data': [addr.to_dict() for addr in data], 'message': '查询成功！'})
        else:
            return jsonify({'code': 0, 'data': {}, 'message': '无地址！'})
    elif request.method == "POST":
        data = request.json
        opType = request.json.get('type')  # 地址操作类型    1：添加 2：修改 3：删除
        if opType == 1:
            addr = UserAddress(user_id=data['userId'], address_detail=data['addressDetail'], area_code=data['areaCode'],
                               city=data['city'], county=data['county'], isDefault=data['isDefault'], name=data['name'],
                               postal_code=data['postalCode'], province=data['province'], phone=data['tel'])
            db.session.add(addr)
            db.session.commit()
            return jsonify(code=1, data='添加成功！', msg='添加成功！')
        elif opType == 2:
            pass
        elif opType == 3:
            pass
        else:
            return jsonify(code=0, msg="不支持当前操作！")


@bp.route('/user/<uid>/card')
def user_profile(uid):
    usr = User.query.filter_by(id=uid).first()
    msg = "查询成功！"
    if usr:
        data = usr.card()
        return jsonify(code=1, data=data, msg=msg)
    else:
        return jsonify(code=0, data="", msg="未找到用户信息！")


@bp.route('/user/join')
def join():
    res = ProductSku.query.join(Shop, Shop.id == ProductSku.shop_id).with_entities(Shop.id, Shop.name, ProductSku.name,
                                                                                   ProductSku.id,
                                                                                   ProductSku.price).all()
    print(res)
    return 'success'
