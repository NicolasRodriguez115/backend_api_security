from flask import Blueprint
from controllers.productController import find_all, find_all_paginate, find_top_selling

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/top_selling', methods=['GET'])(find_top_selling)
product_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)