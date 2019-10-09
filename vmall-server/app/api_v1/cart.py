from . import bp
from flask import jsonify, request, redirect, url_for
from app.models import *
from flask_jwt_extended import jwt_required, create_refresh_token, create_access_token, get_jwt_identity
from sqlalchemy import desc
import datetime
from sqlalchemy import func


@bp.route('/cart/product', methods=('GET', 'POST'))
@jwt_required
def product():
    """
    修改购物车中商品数量
    op  ：购物车商品操作类型。（ 0 ：添加商品, 1：从购物车删除商品 ,2:修改购物车商品数量）
    """
    uid = get_jwt_identity()
    if request.method == 'POST':
        sku_id = request.json.get('id')
        count = request.json.get('count')
        op_type = request.json.get('type')
        cart_sku_count = Cart.query.filter_by(user_id=uid).count()
        msg = '操作成功！'
        if op_type == 0:
            cart_sku = Cart.query.filter_by(user_id=uid, sku_id=sku_id).first()
            if cart_sku:
                cart_sku.checked = 1
                cart_sku.count += count
            else:
                # 限制购物车商品不能超过100
                if cart_sku_count >= 100:
                    return jsonify(code=0, msg="购物车商品种类超过最大限制！！")
                sku = ProductSku.query.filter_by(id=sku_id).first()
                cart_sku = Cart(user_id=uid, sku_id=sku_id, checked=1, count=1, shop_id=sku.shop_id)
                db.session.add(cart_sku)
        elif op_type == 1:
            cart_sku = Cart.query.filter_by(user_id=uid, sku_id=sku_id).first()
            db.session.delete(cart_sku)
        elif op_type == 2:
            cart_sku = Cart.query.filter_by(user_id=uid, sku_id=sku_id).first()
            cart_sku.checked = 1
            cart_sku.count = count
        else:
            return jsonify(code=0, msg="暂不支持当前操作！")
        db.session.commit()
        return jsonify(code=1, msg=msg)


@bp.route('/cart/products', methods=['GET'])
@jwt_required
def cart_products():
    """
    查询购物车中的所有商品
    """
    if request.method == 'GET':
        uid = get_jwt_identity()
        cart_skus = Cart.query.filter_by(user_id=uid).order_by(desc(Cart.modify_time)).all()
        data = {'totalCounts': 0, 'allChecked': 0, "totalPrice": 0}
        if cart_skus:
            results = db.session.query(Cart).outerjoin(ProductSku, Cart.sku_id == ProductSku.id).filter(
                Cart.user_id == uid).outerjoin(Shop, ProductSku.shop_id == Shop.id).with_entities(
                ProductSku.shop_id, Shop.name).group_by(ProductSku.shop_id).all()
            shop_list = [dict(zip(result.keys(), result)) for result in results]
            data["shops"] = shop_list
            for shop in shop_list:
                shop_products = Cart.query.filter_by(user_id=uid, shop_id=shop["shop_id"]).order_by(
                    desc(Cart.modify_time)).all()
                shop["products"] = [shop_product.to_dict() for shop_product in shop_products]
                checked_shop_products = Cart.query.filter_by(user_id=uid, shop_id=shop["shop_id"], checked=1).all()

                # 根据店铺商品数量和选中商品数量判断店铺是否为全选状态
                shop["checked"] = 1 if len(shop_products) == len(checked_shop_products) else 0
            # 根据购物车商品数量和选中商品数量判断是否为全选状态
            cart_checked_skus = Cart.query.filter_by(user_id=uid, checked=1).all()
            data["allChecked"] = 1 if len(cart_checked_skus) == len(cart_skus) else 0

            # 查询选中商品数量
            results = Cart.query.filter_by(user_id=uid, checked=1).with_entities(
                func.sum(Cart.count).label('totalCount')).all()
            count = [dict(zip(result.keys(), result)) for result in results]
            if count[0]['totalCount']:
                data['totalCounts'] = int(count[0]['totalCount'])
            # 查询选中商品价格
            results = db.session.query(Cart).outerjoin(ProductSku, Cart.sku_id == ProductSku.id).filter(
                Cart.user_id == uid, Cart.checked == 1).with_entities(
                func.sum(Cart.count * ProductSku.price).label('totalPrice')).all()
            price = [dict(zip(result.keys(), result)) for result in results]
            if price[0]['totalPrice']:
                data['totalPrice'] = int(price[0]['totalPrice'])
            return jsonify({
                'code': 1,
                'data': data
            })
        else:
            return jsonify({'code': 0, "msg": "你的购物车空空如也！"})


@bp.route('/cart/products/check', methods=['POST'])
@jwt_required
def products_check():
    """
    修改购物车中商品的选择状态
    request:
    return: [ sku_id1,sku_id2]
    """
    uid = get_jwt_identity()
    if request.method == 'POST':
        # 修改购物车商品check状态
        # 修改类型 m_type 0：所有商品 1：店铺 2：单个商品
        # 修改check状态 c_type 0：unchecked 1:checked,
        # pid :商品 sku id
        # shop_id :店铺id
        m_type = request.json.get('m_type')
        c_type = request.json.get('c_type')
        pid = request.json.get('pid')
        shop_id = request.json.get('shop_id')
        msg = "操作成功！"
        if m_type in [0, 1, 2] and c_type in [0, 1]:
            print(request.json)
            if m_type == 0:
                db.session.query(Cart).filter(Cart.user_id == uid).update({Cart.checked: c_type})
            elif m_type == 1 and shop_id:
                results = db.session.query(Cart).filter(Cart.user_id == uid).outerjoin(ProductSku,
                                                                                       Cart.sku_id == ProductSku.id).filter(
                    ProductSku.shop_id == shop_id).all()
                for result in results:
                    result.checked = c_type
            elif m_type == 2:
                db.session.query(Cart).filter(Cart.user_id == uid, Cart.sku_id == pid).update({Cart.checked: c_type})
            else:
                return jsonify(code=0, mgs="参数错误！")
            db.session.commit()
            return jsonify(code=1, mgs=msg)
        else:
            msg = "参数错误！"
            return jsonify(code=0, mgs=msg)
