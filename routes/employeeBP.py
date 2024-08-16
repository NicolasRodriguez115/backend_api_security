from flask import Blueprint
from controllers.employeeController import find_all, products_per_employee

employee_blueprint = Blueprint('employee_bp', __name__)
employee_blueprint.route('/', methods=['GET'])(find_all)
employee_blueprint.route('/products_per_employee', methods=['GET'])(products_per_employee)