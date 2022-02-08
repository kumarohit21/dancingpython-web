from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date

from database.mysql_engine import EmployeesBase


class Employee(EmployeesBase):
    __tablename__ = "employees"

    emp_no = Column(Integer, primary_key=True, index=True)
    birth_date = Column(Date)
    first_name = Column(String(14))
    last_name = Column(String(16))
    gender = Column(String(1))
    hire_date = Column(Date)
