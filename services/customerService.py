from database import db
from models.customer import Customer
from models.order import Order
from models.product import Product
from models.orderProduct import order_product
from sqlalchemy import select, func

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def calc_total_per_customer(threshold):
    query = (
        db.session.query(
            Customer.id,
            Customer.name,
            func.sum(Product.price).label('lifetime_value')
        )
        .join(Order, Customer.id == Order.customer_id)
        .join(order_product, Order.id == order_product.c.order_id)
        .join(Product, order_product.c.product_id == Product.id)
        .group_by(Customer.id, Customer.name)
        .having(func.sum(Product.price) >= threshold)
    )
    results = db.session.execute(query).all()
    return results