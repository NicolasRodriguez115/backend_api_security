from flask import request, jsonify
from models.schemas.employeeSchema import employee_schema, employees_schema
from services import employeeService
from marshmallow import ValidationError

def find_all():
    all_employees = employeeService.find_all()
    return employees_schema.jsonify(all_employees), 200