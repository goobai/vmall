from . import bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import *
from flask import jsonify, request
import datetime


@bp.route('/shop/list', methods=['get'])
@jwt_required
def shop_list():
    """查询店铺信息"""
    if request.method == 'GET':
        limit = request.args.get('limit', int)
        page = request.args.get('page', int)
        if not limit or not page:
            return jsonify(code=0, data='参数错误！', msg='参数错误！')
        offset = (int(page) - 1) * int(limit)
        shops = Shop.query.limit(int(limit)).offset(offset).all()
        total = Shop.query.count()
        data = [shop.to_dict() for shop in shops]
        return jsonify(code=1, data={'shop_list': data, 'total': total}, msg='查询成功！')


@bp.route('/shop/create', methods=['post'])
@jwt_required
def shop_create():
    """新增店铺信息"""
    if request.method == 'POST':
        params = request.json
        shop = Shop.query.filter_by(name=request.json.get('name')).first()
        if shop:
            return jsonify(code=0, data='商品名称已存在，请更换后再提交', msg='操作失败！')
        else:
            shop = Shop(name=params.get('name'), logo=params.get('image'), desc=params.get('desc'),
                        status=params.get('status'))
        db.session.add(shop)
        db.session.commit()
        return jsonify(code=1, data='', msg='操作成功！')


@bp.route('/shop/update', methods=['post'])
@jwt_required
def shop_update():
    """修改店铺信息"""
    if request.method == 'POST':
        params = request.json
        shop = Shop.query.filter_by(id=request.json.get('id')).first()
        if shop:
            shop.name = params.get('name')
            shop.logo = params.get('logo')
            shop.modify_time = datetime.datetime.now()
            shop.status = params.get('status')
            db.session.add(shop)
            db.session.commit()
            return jsonify(code=1, data='', msg='操作成功！')
        else:
            return jsonify(code=0, data='该商铺不存在', msg='操作失败！')


@bp.route('/shop/del', methods=['post'])
@jwt_required
def shop_del():
    """修改店铺信息"""
    if request.method == 'POST':
        shop = Shop.query.filter_by(id=request.json.get('id')).first()
        if shop:
            db.session.delete(shop)
            db.session.commit()
            return jsonify(code=1, data='', msg='操作成功！')
        else:
            return jsonify(code=0, data='该商铺不存在', msg='操作失败！')
