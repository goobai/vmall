from . import bp
from flask import jsonify, request, redirect, url_for
from app.models import *
from flask_jwt_extended import jwt_required, create_refresh_token, create_access_token, get_jwt_identity
from sqlalchemy import desc, func
from app.utils import generate_order_id

"""
   商品单接口：
   1、提交订单
   2、支付订单金额
   3、查询订单状态
   4、查询历史订单
   """


@bp.route('/order/confirm', methods=['POST', 'GET'])
@jwt_required
def order_confirm():
    uid = get_jwt_identity()
    if request.method == "POST":
        """生成订单 订单生成成功后将商品从购物车移除"""
        products = request.json.get('products')  # 订单中的商品及其对应数量
        address_id = request.json.get('address_id')  # 收货地址
        # coupon = request.json.get('coupon')  # 优惠券
        if products:

            # 如果存在跨店商品，根据店铺拆分订单，每个店铺所有商品对应一个订单
            for shop in products:
                order_id = generate_order_id(uid=uid)
                if not order_id:
                    return jsonify(code=0, data={}, msg="订单生成失败！")
                new_order = Order(user_id=uid, user_address_id=address_id, shop_id=shop['shop_id'], order_id=order_id)
                db.session.add(new_order)
                amount = 0
                # 将每个店铺的商品添加到订单商品表
                for product in shop['products']:
                    p_sku = ProductSku.query.filter_by(id=product['id']).first()
                    c_sku = Cart.query.filter_by(sku_id=product['id'], user_id=uid).first()
                    total_price = product['count'] * p_sku.price
                    order_product = OrderProduct(order_id=order_id, sku_id=p_sku.id, price=p_sku.price,
                                                 count=product['count'], total_price=total_price, shop_id=p_sku.shop_id)
                    db.session.add(order_product)
                    db.session.delete(c_sku)
                    amount = amount + total_price
                    new_order.total_price = amount
                order_payment = OrderPayment(order_id=order_id, amount=amount)
                db.session.add(order_payment)
            db.session.commit()
            data = ""
            return jsonify(code=1, data=data, msg="下单成功！")
        else:
            return jsonify(code=0, data={}, msg="参数错误！")
    if request.method == "GET":
        """获取订单信息"""
        order_id = request.args.get('order_id')


@bp.route('/order/pay')
def order_pay():
    """
    用户支付成功后根据店铺进行订单拆分
    :return:
    """
    uid = get_jwt_identity()
    if request.method == "POST":
        """支付"""
        order_id = request.json.get('order_id')
    # region
    # endregion


@bp.route('/order/confirm/products/', methods=['POST'])
@jwt_required
def product_confirm():
    """获取订单确认商品"""
    if request.method == "POST":
        """查询购物车中选中商品，并且返回选中商品名，价格，数量，店铺名"""
        uid = get_jwt_identity()
        cart_skus = Cart.query.filter_by(user_id=uid).order_by(desc(Cart.modify_time)).all()
        data = {'totalCounts': 0, "totalPrice": 0}
        if cart_skus:
            results = db.session.query(Cart).outerjoin(ProductSku, Cart.sku_id == ProductSku.id).filter(
                Cart.user_id == uid, Cart.checked == 1).outerjoin(Shop, ProductSku.shop_id == Shop.id).with_entities(
                ProductSku.shop_id, Shop.name).group_by(ProductSku.shop_id).all()
            shop_list = [dict(zip(result.keys(), result)) for result in results]
            data["shops"] = shop_list
            for shop in shop_list:
                shop_products = Cart.query.filter_by(user_id=uid, shop_id=shop["shop_id"], checked=1).order_by(
                    desc(Cart.modify_time)).all()
                shop["products"] = [shop_product.to_dict() for shop_product in shop_products]
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


@bp.route('/orders', methods=["POST"])
@jwt_required
def order_info():
    """查询订单信息
        返回：订单号 ，商品 ，总价"""
    uid = get_jwt_identity()
    # 订单状态 0:生成订单，待付款 ；1：付款完成，待发货；2：发货完成，物流中，待确认收货 ；3：确认收货，待评价 4：订单完成
    order_status = request.json.get('orderStatus')
    offset = request.json.get('offset')
    limit = 10
    msg = "订单查询成功！"
    if order_status == 0:
        orders = Order.query.filter_by(user_id=uid, order_status=order_status).order_by(desc(Order.create_time)).limit(
            limit).offset(offset).all()
        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data=data, msg=msg)
    elif order_status == 1:
        orders = Order.query.filter_by(user_id=uid, order_status=order_status).order_by(desc(Order.create_time)).limit(
            limit).offset(offset).all()
        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data=data, msg=msg)
    elif order_status == 2:
        orders = Order.query.filter_by(user_id=uid, order_status=order_status).order_by(desc(Order.create_time)).limit(
            limit).offset(offset).all()

        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data=data, msg=msg)
    elif order_status == 3:
        orders = Order.query.filter_by(user_id=uid, order_status=order_status).order_by(desc(Order.create_time)).limit(
            limit).offset(offset).all()
        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data=data, msg=msg)
    elif order_status == 4:
        orders = Order.query.filter_by(user_id=uid, order_status=order_status).order_by(desc(Order.create_time)).limit(
            limit).offset(offset).all()
        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data=data, msg=msg)
    elif order_status == 5:
        orders = Order.query.filter_by(user_id=uid).order_by(desc(Order.create_time)).limit(
            limit).offset(offset).all()
        print(orders)
        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data=data, msg=msg)
    else:
        return jsonify(code=0, msg="查询失败")
