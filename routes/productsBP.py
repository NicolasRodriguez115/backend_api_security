from flask import Blueprint
from controllers.productController import find_all

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['GET'])(find_all)