from flask import Blueprint
from controllers.productController import find_all, find_all_paginate, find_top_selling, find_total_quantity_by_date

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/top_selling', methods=['GET'])(find_top_selling)
product_blueprint.route('/quantity_by_date/<string:date>', methods=['GET'])(find_total_quantity_by_date)
product_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)