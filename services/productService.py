from database import db
from models.product import Product

from sqlalchemy import select

def find_all():
    query = select(Product)
    all_products= db.session.execute(query).scalars().all()
    return all_products