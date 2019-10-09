from flask import Blueprint, request, jsonify

bp = Blueprint('api', __name__)

from . import token
from . import user
from . import articles
from . import seckills
from . import product
from . import cart
from . import order
from . import chat
from . import shop
from . import image
