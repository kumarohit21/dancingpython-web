from typing import Optional
from fastapi import APIRouter, Depends

from database.repo import employees_repo
from database.repo import dependency
from sqlalchemy.orm import Session
from pydantic import parse_obj_as

from schema.employees import EmployeeData

router = APIRouter()


@router.get("/employee/{emp_no}", response_model=EmployeeData)
def read_item(emp_no: int, db: Session  = Depends(dependency.get_db)):
    data =  employees_repo.get_employee_by_id(emp_no,db )
    data =  parse_obj_as(EmployeeData, data)