from flask import Blueprint
from controllers.employeeController import find_all

employee_blueprint = Blueprint('employee_bp', __name__)
employee_blueprint.route('/', methods=['GET'])(find_all)