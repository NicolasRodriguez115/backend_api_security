from database import db
from models.order import Order
from sqlalchemy import select

def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders

def find_all_paginate(page,per_page):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders

