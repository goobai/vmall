from . import bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import *
from flask import jsonify, request


@bp.route('/order/list')
@jwt_required
def order_list():
    """订单列表查询

    """
    if request.method == 'GET':
        limit = request.args.get('limit', type=int)
        page = request.args.get('page', type=int)
        if not limit or not page:
            return jsonify(code=0, data='参数错误！', msg='参数错误！')
        offset = (int(page) - 1) * int(limit)
        orders = Order.query.limit(int(limit)).offset(offset).all()
        total = Order.query.count()
        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data={'order_list': data, 'total': total}, msg='查询成功！')


@bp.route('/order/search')
@jwt_required
def order_search():
    """订单查询

    """
    if request.method == 'GET':
        limit = request.args.get('limit', type=int)
        page = request.args.get('page', type=int)
        order_id = request.args.get('order_id', type=int)
        order_status = request.args.get('order_status', type=int)
        if not limit or not page:
            return jsonify(code=0, data='参数错误！', msg='参数错误！')
        offset = (int(page) - 1) * int(limit)
        total = 0
        orders = []
        if order_id:
            orders = Order.query.filter_by(order_id=order_id).limit(int(limit)).offset(offset).all()
            total = 1
        elif order_status is not None:
            orders = Order.query.filter_by(order_status=order_status).limit(int(limit)).offset(offset).all()
            total = Order.query.filter_by(order_status=order_status).count()
        data = [order.to_dict() for order in orders]
        return jsonify(code=1, data={'order_list': data, 'total': total}, msg='查询成功！')



