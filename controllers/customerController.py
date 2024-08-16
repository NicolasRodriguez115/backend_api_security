from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from utils.util import admin_required

def login():
    try:
        credentials = request.json
        token = customerService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages':'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages':'Invalid username or password'}), 401

def save():

    try:
       
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400

@admin_required
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers),200

def calc_total_per_customer(threshold):
    if threshold >= 0:
        result = customerService.calc_total_per_customer(threshold)
        return customers_schema.jsonify(result), 200
    else:
        return jsonify({'message': 'Invalid threshold value'}), 404