from flask import Blueprint
from controllers.customerController import save, find_all, login, calc_total_per_customer

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/login', methods=['POST'])(login)
customer_blueprint.route('/lifetime_value/<int:threshold>', methods=['GET'])(calc_total_per_customer)
