from . import bp
from app.models import User
from flask import jsonify, request, make_response
from flask_jwt_extended import (
    jwt_required, jwt_refresh_token_required, create_access_token, create_refresh_token,
    get_jwt_identity, get_raw_jwt, get_jwt_claims
)
from app.decorator import jsonp
from flask import g


@bp.route('/token', methods=['POST'])
@jsonp
def gen_token():
    """
    生成用户token
    :return: access_token,refresh_token
    """
    if request.method == 'POST':
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 0
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 0
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id, user_claims=user.to_dict())
            refresh_token = create_refresh_token(identity=user.id)
            return jsonify(
                {'code': 1, 'data': {'access_token': access_token, 'refresh_token': refresh_token}, 'message': '登陆成功！'}

            )
        else:
            return jsonify({'code': 0, 'data': {}, "msg": "Bad username or password"})


@bp.route('/token', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    uid = get_jwt_identity()
    print(uid)
    access_token = create_access_token(identity=uid)
    return jsonify({'code': 1, 'data': {'access_token': access_token}, 'message': '获取成功！'})
