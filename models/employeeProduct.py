from database import db, Base

employee_product = db.Table(
    'employee_Product',
    Base.metadata,
    db.Column('employee_id', db.ForeignKey('Employees.id'), primary_key=True),
    db.Column('product_id', db.ForeignKey('Products.id'), primary_key=True)
)