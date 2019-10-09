from flask import Blueprint

bp = Blueprint('admin', __name__)

from . import product
from . import shop
from . import order
from . import user
from . import image
