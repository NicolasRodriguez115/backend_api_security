from database import db
from models.customer import Customer
from sqlalchemy import select

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers
