from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError

def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 200