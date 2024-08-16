from marshmallow import fields
from . import ma

class EmployeeSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    product = fields.Nested('ProductSchema', many=True)

    class Meta:
        fields = ('id', 'name', 'email', 'phone', 'product', 'total_products')
    
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)