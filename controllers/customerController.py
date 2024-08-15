from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError

def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200