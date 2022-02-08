from sqlalchemy.orm import Session
from app.database.models.employees import Employee

def get_employee_by_id(emp_no: int, db: Session):
    query = db.query(Employee).filter(Employee.emp_no,emp_no)
    return query.one()

