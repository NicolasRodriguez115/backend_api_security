from database import db
from models.employee import Employee
from models.product import Product
from models.employeeProduct import employee_product
from sqlalchemy import select, func

def find_all():
    query = select(Employee)
    all_employees = db.session.execute(query).scalars().all()
    return all_employees

def products_per_employee():
    query = (
        select(
            Employee.name, func.count(Product.id).label('total_products')
        )
        .outerjoin(employee_product, Employee.id == employee_product.c.employee_id)
        .outerjoin(Product, Product.id == employee_product.c.product_id)
        .group_by(Employee.name)
    )

    result = db.session.execute(query).all()
    return result
