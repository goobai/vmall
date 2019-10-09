from . import bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import *
from flask import jsonify, request


# @bp.route('/products')
# @jwt_required
# def products():
#     """查看所有商品"""
#     return ''


@bp.route('/order')
def order():
    """查看或修改某个商品"""
    pass
