from flask import Blueprint
from controllers.customerController import find_all

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['GET'])(find_all)