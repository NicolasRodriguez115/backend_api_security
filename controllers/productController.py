from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError

def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 200

def find_all_paginate():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    products = productService.find_all_paginate(page, per_page)
    return products_schema.jsonify(products), 200

def find_top_selling():
    result = productService.find_top_selling()
    return products_schema.jsonify(result), 200