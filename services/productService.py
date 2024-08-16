from database import db
from models.product import Product
from models.order import Order
from models.orderProduct import order_product
from sqlalchemy import select, func, desc

def find_all():
    query = select(Product)
    all_products= db.session.execute(query).scalars().all()
    return all_products

def find_all_paginate(page,per_page):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products

def find_top_selling():
    query = (
        select(
            Product.name, func.count(Order.id).label('amount_sold')
        )
        .outerjoin(order_product, Product.id == order_product.c.product_id)
        .outerjoin(Order, Order.id == order_product.c.order_id)
        .group_by(Product.name)
        .order_by(desc('amount_sold'))
    )

    result = db.session.execute(query).all()
    return result

def find_total_quantity_by_date(date):
    query = (
        select(
            Product.name,
            func.sum(order_product.c.quantity).label('total_quantity')
        )
        .join(order_product, Product.id == order_product.c.product_id)
        .join(Order, Order.id == order_product.c.order_id)
        .filter(Order.date == date)
        .group_by(Product.name)
    )

    result = db.session.execute(query).all()
    return result