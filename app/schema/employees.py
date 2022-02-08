from datetime import date
from typing import Optional
from pydantic import BaseModel


class EmployeeData(BaseModel):
    emp_no: Optional[int]
    birth_date: Optional[date]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    hire_date: Optional[date]

    class Config:
        orm_mode = True
