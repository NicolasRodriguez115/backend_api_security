from marshmallow import fields
from . import ma

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=False)
    price = fields.Integer(required=True)

    class Meta:
        fields = ("id", 'name', 'price', 'total_quantity')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)