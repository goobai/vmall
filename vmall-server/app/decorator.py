from functools import wraps
from flask import request, current_app, jsonify
from flask_jwt_extended import get_jwt_identity


def jsonp(func):
    """Wraps JSONified output for JSONP requests."""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)

    return decorated_function


def permission(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        uid = get_jwt_identity()
        return jsonify(code=0, msg="未授权")

    return decorated_function



