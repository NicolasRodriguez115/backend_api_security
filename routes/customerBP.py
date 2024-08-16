from flask import Blueprint
from controllers.customerController import find_all, calc_total_per_customer

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/lifetime_value/<int:threshold>', methods=['GET'])(calc_total_per_customer)
