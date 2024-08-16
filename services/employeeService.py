from database import db
from models.employee import Employee
from sqlalchemy import select

def find_all():
    query = select(Employee)
    all_employees = db.session.execute(query).scalars().all()
    return all_employees
