from database import db
from models.order import Order
from sqlalchemy import select

def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders
