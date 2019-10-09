from flask import Blueprint, request, jsonify

bp = Blueprint('main', __name__)

from . import routes
