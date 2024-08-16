from flask import jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError

def find_all():
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200

def find_all_paginate():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    orders = orderService.find_all_paginate(page, per_page)
    return orders_schema.jsonify(orders), 200



    