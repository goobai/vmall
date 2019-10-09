from . import bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import *
from flask import jsonify, request
import datetime


@bp.route('/product/list', methods=['get'])
@jwt_required
def product_list():
    """查询商品列表"""
    if request.method == 'GET':
        limit = request.args.get('limit', int)
        page = request.args.get('page', int)
        if not limit or not page:
            return jsonify(code=0, data='参数错误！', msg='参数错误！')
        offset = (int(page) - 1) * int(limit)
        products = ProductSku.query.limit(int(limit)).offset(offset).all()
        total = ProductSku.query.count()
        data = [product.to_dict() for product in products]
        return jsonify(code=1, data={'product_list': data, 'total': total}, msg='查询成功！')


@bp.route('/product/create', methods=['post'])
@jwt_required
def product_create():
    """新增商品"""
    if request.method == 'POST':
        params = request.json
        spu_name = request.json.get('name')
        spu_title = request.json.get('title')
        shop_id = request.json.get('shop_id')
        price = request.json.get('price')
        spu = ProductSpu(shop_id=shop_id, title=spu_title, name=spu_name, price=price)
        db.session.add(spu)
        db.session.commit()

        spu_name = request.json.get('name')
        spu_name = request.json.get('name')
        spu_name = request.json.get('name')
        spu_name = request.json.get('name')
        product = ProductSku.query.filter_by(name=request.json.get('name')).first()
        if product:
            return jsonify(code=0, data='商品名称已存在，请更换后再提交', msg='操作失败！')
        else:
            product = ProductSku(name=params.get('name'), logo=params.get('logo'), desc=params.get('desc'),
                                 status=params.get('status'))
        db.session.add(product)
        db.session.commit()
        return jsonify(code=1, data='', msg='操作成功！')


@bp.route('/product/update', methods=['post'])
@jwt_required
def product_update():
    """修改商品信息"""
    if request.method == 'POST':
        params = request.json
        sku_id = request.json.get('id')
        if sku_id:
            name = params.get('name')
            price = params.get('price')
            stock = params.get('stock')
            modify_time = datetime.datetime.now()
            status = params.get('status')
            ProductSku.update_sku(sku_id, name=name, price=price, stock=stock, modify_time=modify_time, status=status)
            return jsonify(code=1, data='', msg='操作成功！')
        else:
            return jsonify(code=0, data='该商品不存在', msg='操作失败！')


@bp.route('/product/del', methods=['post'])
@jwt_required
def product_del():
    """删除商品"""
    if request.method == 'POST':
        sku_id = request.json.get('id')
        if sku_id:
            ProductSku.del_sku(sku_id)
            return jsonify(code=1, data='删除成功！', msg='操作成功！')
        else:
            return jsonify(code=0, data='请求参数错误', msg='操作失败！')
