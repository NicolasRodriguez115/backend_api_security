from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError

def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200

def calc_total_per_customer(threshold):
    if threshold >= 0:
        result = customerService.calc_total_per_customer(threshold)
        return customers_schema.jsonify(result), 200
    else:
        return jsonify({'message': 'Invalid threshold value'}), 404