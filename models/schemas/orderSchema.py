from marshmallow import fields
from . import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.Nested("ProductSchema", many=True)
    customer = fields.Nested('CustomerOrderSchema')

    class Meta:
        fields = ('id', 'date', 'customer_id', 'total_value', 'products', 'customer')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)