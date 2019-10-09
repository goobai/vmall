from flask import jsonify, send_from_directory, current_app

from app.models import *
from . import bp


@bp.route('/shop/<name>/card')
def card(name):
    shop = Shop.query.filter_by(name=name).first()
    msg = "查询成功！"
    if shop:
        data = shop.card()
        return jsonify(code=1, data=data, msg=msg)
    else:
        return jsonify(code=0, data="", msg="未找到店铺信息！")


@bp.route('/shop/logo/<filename>')
def shop_logo(filename):
    logo_path = current_app.config['UPLOAD_FOLDER']
    return send_from_directory(logo_path, filename=filename)
