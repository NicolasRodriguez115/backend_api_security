from flask import jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema
from marshmallow import ValidationError
from services import orderService

def find_all():
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200